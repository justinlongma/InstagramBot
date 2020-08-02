import instaloader
import numpy as np

'''Define global variables for more efficient code'''
followers = np.empty(0) #list that stores follower usernames
following = np.empty(0) #list that stores following usernames
follower_id = np.empty(0) #list that stores follower id names (for ghost func)
ghosts = np.empty(0) #list that store ghosts 
ghost_run = False #checks to see if ghost has been run before for efficiency
profile = None ##allows GUI to check ghosts

class InstagramLoader:
    
    '''Constructor to create instaloader instance'''
    def __init__(self, USERNAME, PASSWORD):
        if USERNAME is None and PASSWORD is None:
            return
        
        '''Loads up Instaloader'''
        L = instaloader.Instaloader()
        L.login(USERNAME, PASSWORD)        
        global profile
        profile = instaloader.Profile.from_username(L.context, USERNAME)
        
        
        '''Add Followers of USERNAME to followers list'''
        global followers
        global follower_id
        for follower in profile.get_followers():
            followers = np.append(followers, follower.username)
            follower_id = np.append(follower_id, follower)

        '''Add Users who USERNAME is following to the following list'''
        global following            
        for followee in profile.get_followees():
            following = np.append(following, followee.username)


    '''Returns a np array of usernames of who follows USERNAME'''
    def get_follower_usernames(self):
        return followers
    
    '''Seturns a np array of usernames who the USERNAME is following'''
    def get_following_usernames(self):
        return following

    '''Returns a np array of usernames who USERNAME is following, but not following back USERNAME '''
    def get_fake_usernames(self):
        return np.setdiff1d(following, followers)
    
    '''Returns a np array of usernames who USERNAME is not following, but who are following USERNAME'''
    def get_fan_usernames(self):
        return np.setdiff1d(followers, following)
    
    '''Returns a np array of usernames who have not liken a single post made by USERNAME'''
    def get_ghost_usernames(self):
        global ghosts
        global ghost_run
        if ghost_run == False:
            global profile
            global follower_id
            likes = set()
            for post in profile.get_posts():
                likes = likes | set(post.get_likes())
            ghost_id = set(follower_id) - likes
            for ghost in ghost_id:
                ghosts = np.append(ghosts, ghost.username)  
            ghost_run = True
        return ghosts
            
'''For Testing purposes             
InstagramLoader('INSERT USERNAME HERE', 'INSERT PASSWORD HERE')
'''
