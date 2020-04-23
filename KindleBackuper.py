import os
import time

print("\t\t\tПрограмма KindleBackuper by @Rykov7 v1.0.")
print("\t\t\tСоздаёт резервную копию устройства Kindle Paperwhite.")
print(time.strftime('\t\t\t{}-{}-{}\n'.format('%d','%B','%Y')))

def volume(question):
	vol_acceptable = ['D', 'E', 'F', 'G','H', 'I', 'J', 'K']
	vol = None
	while vol not in vol_acceptable:
		vol = input(question)
		if vol.upper() in vol_acceptable:
			return vol
		else:
			print('Том "' + vol + '"" недопустим. Проверьте раскладку клавиатуры и попробуйте ввести имя тома ещё раз.\n')


def yes_no(source):
	agreement = ""
	while agreement.upper() not in ("N", "Y", "Д", "Н"):
		print('\nВы действительно хотите сделать резервную копию следующих дерикторий и файлов: ')
		for i in source:
			print(i)
		agreement = input("? (Y/N): ")
		if agreement.upper() in ("Y", 'Д'):
			print("Запускаю процесс архивации...")
		elif agreement.upper() in ("N", 'Н'):
			input("Вы отменили создание резервной копии. До свидания!")
		else:
			print("Некорректное значение " + agreement)
	return agreement


def main():
	# 1. List that collected Files and directories to be copied. Double quotes for paths with spaces
	source = [volume('Введите букву ТОМа, присвоенную Kindle Paperwhite: ') + r':\documents']
	
	# 2. Backups must be stored in the primary reserve directory.
	target_dir = volume('Укажите букву ТОМа, в корень которого сохранить резервную копию: ') + ':'

	# 3. Files are placed to an archive.
	# The current date is the name of the subdirectory in the main directory
	today = target_dir + os.sep + time.strftime('%Y-%m-%d')

	# The current time is the name of the zip archive
	now = time.strftime('_%H-%M')
	
	compression_level = 0
	while compression_level not in range(0, 10):
		try:
			compression_level = int(input('\nВыберите уровень сжатия (0-9): '))
		except:
			print("Вы ввели некорректный уровень компрессии.\n")

	# Create a directory if it is not already
	device = 'kindle_'
	target = today + os.sep + device + time.strftime('%Y-%m-%d') + now + ".zip"
	zip_command = "zip -" + str(compression_level) + "rqdgds 250m -UN=UTF8 {0} {1}".format(target, ' '.join(source))
	if not os.path.exists(today):
		os.mkdir(today) # Creating the directory
		print("Каталог успешно создан" + today + '...')

	if yes_no(source).upper() != "N" and os.system(zip_command) == 0:
		print("Резервная копия успешно создана в " + target + " с уровнем сжатия " + str(compression_level) + ".")
		print("Работа завершена.")

	else:
		print("Создание резервной копии НЕ УДАЛОСЬ")


main()
input("Нажмите 'Enter' для выхода.")