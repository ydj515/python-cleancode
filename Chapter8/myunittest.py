#-*- coding: utf-8 -*-

import unittest
from enum import Enum

"""
한 명 이상의 사용자가 변경 내용에 동의하지 않은 경우 머지 리퀘스트가 거절된다(rejected)
아무도 반대하지 않은 상태에서 두 명 이상의 개발자가 동의하면 해당 머지 리퀘스트는 승인된다(approved)
이외의 상태는 보류상태이다(pending)
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


class TestMergeRequestStatus(unittest.TestCase):

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvotes("maintainer")
        self.assertEqual(merge_request.status,MergeRequestStatus.REJECTED)
    
    def test_just_created_is_pending(self):
        self.assertEqual(MergeRequest().status,MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(merge_request.status,MergeRequestStatus.PENDING)

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")
        self.assertEqual(merge_request.status,MergeRequestStatus.APPROVED)

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(Exception, self.merge_request.upvote,"dev1")
    
    def test_cannot_downvote_con_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaisesRegex("종료된 머지 리퀘스트에 투표할 수 없음", self.merge_request.downvote, "dev1")
    