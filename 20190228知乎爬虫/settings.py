COOKIES = {'cookie': '_zap=a8c03525-4dfd-4e25-9cb4-68deaa2c3186; d_c0="AMCh-H07iA6PTiB2UAouvdBx5_x2QkRQKak=|1542440569"; __gads=ID=2ec6cbcad819aa52:T=1542682105:S=ALNI_MaujjBN3NxAp6YQh8P4C5q8zvMu-w; _xsrf=gY28KXF57fYp6BAd0KSczGm5puO5n7YY; capsion_ticket="2|1:0|10:1549238634|14:capsion_ticket|44:N2JmOTA1YjhlMjIzNGRiMmI1NDAzYzhlM2JlNzU5MGQ=|e1a64eb495eb67630f00c5cbae60fb8542a50eef21b549d1b19adaa81c3c7b40"; z_c0="2|1:0|10:1549238635|4:z_c0|92:Mi4xcTBUUUFnQUFBQUFBd0tINGZUdUlEaVlBQUFCZ0FsVk5hODlFWFFCX1RtTzJ5YzEtNzhYTWhpZ0xvbGhwM1pzdzRR|e91937d8092c6bc55b4c2d5d63ae768460be344af8f85a50aef53f47a044648e"; tst=r; q_c1=b1e9c921c6c44f6faca23cf3ddded288|1551227918000|1542440572000; __utma=155987696.2049416871.1551236587.1551236587.1551236587.1; __utmc=155987696; __utmz=155987696.1551236587.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=116a747939468d99065d12a386ab1c5f'}

HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

BASE_URL = 'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default'




def answers_clean_json(jsondata):
    #将问题的回答们改造成depth=1的字典
    newdict = dict()
    newdict['admin_closed_comment'] = jsondata['admin_closed_comment']
    newdict['annotation_action'] = jsondata['annotation_action']
    newdict['answer_type'] = jsondata['answer_type']
    newdict['avatar_url'] = jsondata['author']['avatar_url'].replace('_is', '')
    newdict['user_badge'] = jsondata['author']['badge']
    newdict['user_follower_count'] = jsondata['author']['follower_count']
    newdict['gender'] = jsondata['author']['gender']
    newdict['user_headline'] = jsondata['author']['headline']
    newdict['userid'] = jsondata['author']['id']
    newdict['user_is_advertiser'] = jsondata['author']['is_advertiser']
    newdict['user_name'] = jsondata['author']['name']
    newdict['user_type'] = jsondata['author']['user_type']
    newdict['user_url_token'] = jsondata['author']['url_token']
    newdict['comment_count'] = jsondata['comment_count']
    newdict['content'] = jsondata['content']
    newdict['created_time'] = jsondata['created_time']
    newdict['editable_content'] = jsondata['editable_content']
    newdict['answer_id'] = jsondata['id']
    newdict['answer_collapse_reason'] = jsondata['collapse_reason']
    newdict['answer_collapsed_by'] = jsondata['collapsed_by']
    newdict['answer_is_collapsed'] = jsondata['is_collapsed']
    newdict['answer_is_copyable'] = jsondata['is_copyable']
    newdict['answer_is_labeled'] = jsondata['is_labeled']
    newdict['answer_collapsed_by'] = jsondata['collapsed_by']
    newdict['question_created'] = jsondata['question']['created']
    newdict['question_updated_time'] = jsondata['question']['updated_time']
    newdict['relationship_upvoted_followees'] = jsondata['relationship']['upvoted_followees']
    newdict['relationship_voting'] = jsondata['relationship']['voting']
    newdict['answer_reshipment_settings'] = jsondata['reshipment_settings']
    # 打赏功能是否打开
    newdict['can_open_reward'] = jsondata['reward_info']['can_open_reward']
    newdict['is_rewardable'] = jsondata['reward_info']['is_rewardable']
    newdict['reward_member_count'] = jsondata['reward_info']['reward_member_count']
    newdict['reward_total_money'] = jsondata['reward_info']['reward_total_money']
    newdict['tagline'] = jsondata['reward_info']['tagline']

    newdict['voteup_count'] = jsondata['voteup_count']
    newdict['answer_suggest_edit'] = jsondata['suggest_edit']['reason']
    newdict['answer_suggest_edit_status'] = jsondata['suggest_edit']['status']
    newdict['answer_suggest_edit_tip'] = jsondata['suggest_edit']['tip']
    newdict['answer_suggest_edit_title'] = jsondata['suggest_edit']['title']
    newdict['answer_suggest_edit_tip_unnormal_details_description'] = jsondata['suggest_edit']['unnormal_details'][
        'description']
    newdict['answer_suggest_edit_tip_unnormal_details_description'] = jsondata['suggest_edit']['unnormal_details'][
        'note']
    newdict['answer_suggest_edit_tip_unnormal_details_description'] = jsondata['suggest_edit']['unnormal_details'][
        'reason']
    return newdict