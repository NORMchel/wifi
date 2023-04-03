import subprocess

# Получаем результат выполнения команды "netsh wlan show profiles"

output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Получаем имена всех профилей WiFi

profiles = [i.split(":")[1][1:-1] for i in output if "Все профили пользователей" in i]

# Итерируемся по всем профилям и получаем информацию о каждом

for profile in profiles:

    # Получаем информацию о профиле

    try:

        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')

    except subprocess.CalledProcessError as e:

        print(f"Не удалось получить информацию о профиле {profile}")

        continue

    # Получаем пароль из результатов

    password = [line.split(":")[1][1:-1] for line in results if "Ключ содержит" in line]

    

    # Выводим имя профиля и пароль

    print("{:<30}|  {:<}".format(profile, password[0] if password else ""))
