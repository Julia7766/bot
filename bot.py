import requests
get_user = ()
friendly_bot = ()

#new client input zone
def user_client():
    get_user = user_client()
    result = get_user.input("Пожалуйста, введите ваш запрос: ")
    return result


#chatbot zone: accepted client's answer and say some welcome-phrase
def chat_bot():
    while get_user == user_client():
        print('Здравствуй! Чем могу быть полезен?')
        print('Могу решить ваши любые юридические вопросы и предоставить данные!')
        if get_user != user_client():
           # break


#place, where the request push
#def form_request():
   # pass


#where give a response
#def form_answers():
    #pass


def main():
   get_user = user_client()
   chat_bot()

if __name__ == "__main__":
    main()
