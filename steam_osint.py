from time import sleep
from requests_html import HTMLSession
session = HTMLSession()

banner = '''\033[31m
       .:'                                  `:.
  ::'                                    `::
 :: :.                                  .: ::
  `:. `:.             .             .:'  .:'
   `::. `::           !           ::' .::'
       `::.`::.    .' ! `.    .::'.::'
         `:.  `::::'':!:``::::'   ::'
         :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
       ::: `H TH::.  `!'  .::HT H' :::
       ::..  `THHH:`:   :':HHHT'  ..::
       `::      `T: `. .' :T'      ::'
         `:. .   :         :   . .:'
           `::'               `::'
             :'  .`.  .  .'.  `:
             :' ::.       .:: `:
             :' `:::     :::' `:
              `.  ``     ''  .'
               :`...........':
               ` :`.     .': '
                `:  `"""'  :'   

    EXAMPLE: https://steamcommunity.com/id/xxxxxxxxxxxx
    The Profile Must Be Public

'''
print(banner)


user_scan = str(input('\033[m STEAM ID: '))
p1_friends = [user_scan]
p2_friends = []
both_friend = []
comments = []



try:
    info_url = session.get(p1_friends[0])        
except:    
    print('The URL is invalid')

#PROFILE 01 INFORMATION
profile = session.get(p1_friends[0] + '/friends')
friends01 = profile.html.find('.selectable_overlay')
p1_comments = session.get(p1_friends[0] +'/allcomments')
user_c = p1_comments.html.find('.whiteLink.persona_name_text_content')
pag_comments = p1_comments.html.find('.hoverunderline.commentthread_author_link')
p1_friends.remove(p1_friends[0])
for f01 in friends01:
    p1_friends.append(str(f01.absolute_links)[2:-2])

while True:
        sleep(1)
        if len(p1_friends) != 0:                   
            #PROFILE 02 INFORMATION
            profile02 = session.get(p1_friends[0] + '/friends')
            friends02 = profile02.html.find('.selectable_overlay')
            p1_friends.remove(p1_friends[0])
            if len(friends02) != 0:
                for f02 in friends02:
                    p2_friends.append(str(f02.absolute_links)[2:-2])
                #THERE ARE FRIENDS?
                for check in p1_friends:
                    if check in p2_friends:
                        both_friend.append(check)
                p2_friends.clear()
            else:
                p1_friends.remove(p1_friends[0])
        else:
            for c  in  range(0, len(pag_comments)):
                comments.append(str(pag_comments[c].absolute_links)[2:-2])
            print('\033[31m','-'*50)
            print('User Scaning:',user_c[0].text.center(30))
            print(f'Close Friends Found: {len(set(both_friend))}')
            print(f'Comment Found: {len(comments)}')
            print('-'*50,'\033[m')
            for both in set(both_friend):
                if both_friend.count(both) >= 1 and comments.count(both) > 0:
                    print(f'[ + ] {both}')
                    print(' '*4,f' • \033[32mComments in Your Profile: {comments.count(both)}\033[m')
                else:
                    print(f'[ + ] {both}')
            break