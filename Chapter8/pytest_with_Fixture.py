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
    """
    pytest.fixture를 사용하면 재사용 가능한 기능을 쉽게 만들 수 있음
    """
    @pytest.fixture
    def rejected_mr(self):
        merge_request = MergeRequest()
        merge_request.downvotes("dev1")
        merge_request.upvote("dev2")
        merge_request.upvote("dev3")
        merge_request.downvotes("dev4")

        return merge_request


    def test_simple_rejected(rejected_mr):
        assert rejected_mr.status== MergeRequestStatus.REJECTED
    
    def test_just_created_is_pending(self):
        assert rejected_mr.status == MergeRequestStatus.PENDING

    def test_rejected_with_approvals(rejected_mr):
        rejected_mr.upvote("dev2")
        rejected_mr.upvote("dev3")
        assert rejected_mr.status == MergeRequestStatus.PENDING

    def test_rejected_to_pending(rejected_mr):
        rejected_mr.upvote("dev1")
        assert rejected_mr.status == MergeRequestStatus.PENDING

    def test_rejected_to_approved(rejected_mr):
        rejected_mr.upvote("dev1")
        rejected_mr.upvote("dev1")
        assert rejected_mr.status == MergeRequestStatus.APPROVED

        