import requests
import datetime

def convert_date(x):
    return datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime('%m-%d-%Y  %H:%M:%S')

def ask_again():
    while True:
        response4 = raw_input('Would you like to find more news articles? \n[1] Yes \n[2] No\n')
        if response4 == '1':
            return True
        elif response4 == '2':
            return False
        else:
            print '\nplease enter either 1 or 2 only\n'
            continue

def read():
    while True:
        response = raw_input('Welcome to Command Line News! Please make a choice: \n[1] Top Headlines \n[2] Search\n')
        if response == '1':
            url = ('https://newsapi.org/v2/top-headlines?'
                   'country=us&'
                   'apiKey=8b1de87e74b346159f977fa840661553')
            response1 = requests.get(url)
            response1 = response1.json()

            for i in response1['articles']:
                print '\t*', i['title']
                print '\t\t-', convert_date(i['publishedAt'])
                if i['description'] == None:
                    pass
                else:
                    print '\t\t-', i['description']
                print

        elif response == '2':
            response2 = raw_input('Enter your search term:\n')
            string_url = 'https://newsapi.org/v2/everything?''q='+str(response2)+'&''from=2018-02-23&''sortBy=popularity&''apiKey=8b1de87e74b346159f977fa840661553'
            response5 = requests.get(string_url)
            response5 = response5.json()
            for i in response5['articles']:
                print '\t*', i['title']
                print '\t\t-', convert_date(i['publishedAt'])
                if i['description'] == None:
                    pass
                else:
                    print '\t\t-', i['description']
                print
        else:
            print '\nPlease enter either 1 or 2\n'
            continue

        if ask_again() == True:
            continue
        else:
            print('\nGoodbye!')
            break

def main():
    try:
        read()
    except:
        print('Could not recognize that character')

if __name__ == '__main__':
    main()
