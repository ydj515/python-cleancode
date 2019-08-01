#-*- coding: utf-8 -*-

import pytest
from enum import Enum

"""
unittest의 assertEqual문을 간소화 하게 assert로 대체 가능
"""
class MergeRequestStatus(Enum): # enum class
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "close"

class MergeRequest:
    def __init__(self):
        self._context = {"upvotes": set(), "downvotes": set()}
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise Exception("종료된 머지 리퀘스트에 투표할 수 없음")
    
    @property
    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) <= 2:
            return MergeRequestStatus.APPROVED
            return MergeRequestStatus.PENDING
    
    def upvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvotes(self, by_user):
        self._cannot_vote_if_closed()
        self._context["downvotes"].add(by_user)
        self._context["upvotes"].discard(by_user)


class TestMergeRequestStatus():

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvotes("maintainer")
        assert merge_request.status == MergeRequestStatus.REJECTED
    
    def test_just_created_is_pending(self):
        assert MergeRequest().status == MergeRequestStatus.PENDING

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        assert merge_request.status == MergeRequestStatus.PENDING

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")
        assert merge_request.status == MergeRequestStatus.APPROVED

    def test_invalid_types(self):
        merge_request = MergeRequest()
        pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})

    def test_cannot_upvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        pytest.raises(Exception, merge_request.upvote, "dev1")
        
        with pytest.raises(Exception, match="종료된 머지 리퀘스트에 투표할 수 없음"):
            merge_request.downvotes("dev1")
