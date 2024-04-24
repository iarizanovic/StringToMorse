from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Morse_code")
driver.maximize_window()

dictionary = {' ': '    '}
for i in range(1, 92):
    if i == 45 or i == 50:
        letter = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[45]/td[2]/b[2]").text
        continue

    try:
        letter = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[2]/b").text
    except:
        try:
            letter = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[2]/a/b[2]").text
        except:
            letter = "no"

    morse = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[3]/span/span/a/span[2]/span").text
    letters = letter.split(', ')
    for l in letters:
        if len(l) == 1:
            dictionary[l] = morse
driver.close()

# Convert to morse
words = input("Enter the string to convert to morse: ")
words_morse = ""
for w in words:
    words_morse += dictionary[w]
print("Morse: ", words_morse)

# Decode
words_test = ""
words_morse += " "
while len(words_morse) > 1:
    for (k, v) in dictionary.items():
        if words_morse[:len(v)+1] == v + " ":
            words_test += k
            words_morse = words_morse[len(v):len(words_morse)]
            break

print("Decode: ", words_test)
