class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])

        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)

        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        users = self.followMap[userId] | {userId}

        for uid in users:
            tweets = self.tweetMap[uid]

            if tweets:
                i = len(tweets) - 1
                count, tweetId = tweets[i]
                heapq.heappush(heap, (count, tweetId, uid, i - 1))

        while heap and len(result) < 10:
            count, tweetId, uid, i = heapq.heappop(heap)
            result.append(tweetId)

            if i >= 0:
                count, tweetId = self.tweetMap[uid][i]
                heapq.heappush(heap, (count, tweetId, uid, i - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
