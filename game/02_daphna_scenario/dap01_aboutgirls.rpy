################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_request_01: #LV.1 (Whoring = 0 - 2)
    $hero(m,"#(Я расспрошу ее о ее подружках...)")
    menu:
        "\"(Да, сделаем это.)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $hero("Ладно...// Просто расскажи что нового у тебя.")


