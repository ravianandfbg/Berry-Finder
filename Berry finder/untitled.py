def programStartListener1():
    global game_in_progress, Live, time_remaining, score, player_name
    Canvas.goToCanvas("appScreen_1")


onProgramStart(programStartListener1)


def uiButtonClickEventListener1():
    global game_in_progress, Live, time_remaining, score, player_name
    Canvas.goToCanvas("appScreen_1")


Button.onClickEvent('replay_Button', uiButtonClickEventListener1)


def messageListener1():
    global game_in_progress, Live, time_remaining, score, player_name
    game_in_progress = 0
    Canvas.goToCanvas("appScreen_3")
    Label.setText('fs_Label', score)
    Label.setText('hs_Label', (int((CloudData.getKeyValue('high_score_key')))))
    Label.setText('hsname_Label', (CloudData.getKeyValue('high_scorer_name_key')))


Message.onMessageReceived('show_final_scoreboard', messageListener1)


def messageListener2():
    global game_in_progress, Live, time_remaining, score, player_name
    while not (time_remaining == 0 or Live == 0):
        Time.sleep(1)
        time_remaining -= 1
        Label.setText('Time value_Label', time_remaining)
        if time_remaining == 0:
            if score > (int((CloudData.getKeyValue('high_score_key')))):
                CloudData.setKeyValue('high_score_key', score)
                CloudData.setKeyValue('high_scorer_name_key', player_name)
                AppElement.show("congrates_Label")
            AppElement.show("thanks_Label")
            Message.broadcastMessage('show_final_scoreboard')


Message.onMessageReceived('start_the_timer', messageListener2)


def uiButtonClickEventListener2():
    global game_in_progress, Live, time_remaining, score, player_name
    AppElement.hide("wish_Label")
    AppElement.hide("thanks_Label")
    AppElement.hide("congrates_Label")
    Canvas.goToCanvas("appScreen_2")
    player_name = Textbox.getText('player_name_Textbox')
    score = 0
    Live = 3
    Label.setText('value_Label', score)
    Label.setText('Live value_Label_1', Live)
    time_remaining = 30
    game_in_progress = 1
    Label.setText('Time value_Label', time_remaining)
    Message.broadcastMessage('start_the_timer')
    while game_in_progress == 1:
        AppElement.setProperty('strawberry_Button', AppElementProperty.LEFT, (random.randint(40, 750)))
        AppElement.setProperty('strawberry_Button', AppElementProperty.TOP, (random.randint(40, 550)))
        Time.sleep(1)


Button.onClickEvent('play_Button', uiButtonClickEventListener2)


def uiButtonClickEventListener3():
    global game_in_progress, Live, time_remaining, score, player_name
    Live -= 1
    Label.setText('Live value_Label_1', Live)
    if Live == 0:
        AppElement.show("wish_Label")
        Message.broadcastMessage('show_final_scoreboard')


Button.onClickEvent('background_Button', uiButtonClickEventListener3)


def uiButtonClickEventListener4():
    global game_in_progress, Live, time_remaining, score, player_name
    AppElement.setProperty('strawberry_Button', AppElementProperty.LEFT, (random.randint(40, 750)))
    AppElement.setProperty('strawberry_Button', AppElementProperty.TOP, (random.randint(40, 550)))
    score += 1
    Label.setText('value_Label', score)


Button.onClickEvent('strawberry_Button', uiButtonClickEventListener4)


