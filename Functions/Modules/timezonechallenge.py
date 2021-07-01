import pytz
import datetime


def time_in_zone(country):
    tz_to_display = pytz.timezone(country)
    local_time = datetime.datetime.now(tz=tz_to_display)
    return local_time


def main():
    print(f'============================================================================================================\n'
          f'\t\t\t\t\t\tWelcome to Time Zone Program!\n'
          f'============================================================================================================\n'
          f'\t\t\t\tActual time in Sweden: {time_in_zone("Europe/Stockholm")} \n'
          f'____________________________________________________________________________________________________________\n'
          f'Choose a place to display their local time:\n'
          f'1. Sao Paolo, 2. New York, 3. Lisbon, 4. Sydney, 5. Honolulu, 6. Lima, 7. Casablanca 8. Tehran 9. Shanghai\n'
          f'\t\t\t\t\t\tPush 0 to quit\n'
          f'============================================================================================================')

    while True:
        user_choice = int(input("Type your choice: "))

        if user_choice == 1:
            print("Time in Sao Paolo: {}\n".format(time_in_zone('America/Sao_Paulo')))
        if user_choice == 2:
            print("Time in New York: {}\n".format(time_in_zone('America/New_York')))
        if user_choice == 3:
            print("Time in Lisbon: {}\n".format(time_in_zone('Europe/Lisbon')))
        if user_choice == 4:
            print("Time in Sydney: {}\n".format(time_in_zone('Australia/Sydney')))
        if user_choice == 5:
            print("Time in Honolulu: {}\n".format(time_in_zone('Pacific/Honolulu')))
        if user_choice == 6:
            print("Time in Lima: {}".format(time_in_zone('America/Lima')))
        if user_choice == 7:
            print("Time in Casablanca: {}\n".format(time_in_zone('Africa/Casablanca')))
        if user_choice == 8:
            print("Time in Tehran: {}\n".format(time_in_zone('Asia/Tehran')))
        if user_choice == 9:
            print("Time in Shanghai: {}\n".format(time_in_zone('Asia/Shanghai')))
        if user_choice == 0:
            break


if __name__ == '__main__':
    main()
