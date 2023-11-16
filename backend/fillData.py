import requests

url = 'http://127.0.0.1:5001'
headers = {'Content-Type': 'application/json'}


read_responses = []

############################## clearing database ##############################

x = requests.delete(url + '/clear_database', headers=headers, json={})
read_responses.append(x)
print(x.text)
############################## adding new projects ##############################
x = requests.post(url + '/signup', headers=headers, json={
    "email": "test@gmail.com",
    "name": "Andrea",
    "role": "User",
    "unit": "test unit",
    "jobTitle": "undersköterska"
})
x = requests.post(url + '/signup', headers=headers, json={
    "email": "test2@gmail.com",
    "name": "test2",
    "role": "Admin",
    "unit": "test unit",
    "jobTitle": "undersköterska"
})
x = requests.post(url + '/signup', headers=headers, json={
    "email": "test3@gmail.com",
    "name": "test3",
    "role": "User",
    "unit": "test unit",
    "jobTitle": "undersköterska"
})
x = requests.post(url + '/signup', headers=headers, json={
    "email": "test4@gmail.com",
    "name": "test4",
    "role": "User",
    "unit": "test unit",
    "jobTitle": "undersköterska"
})

h = requests.post(url + '/login', headers=headers, json={"user_id": 1})
response_data = h.json()
token = response_data.get("token", "")
headers = {'Content-Type': 'application/json', "Authorization": "Bearer " + token}
read_responses.append(x)
# change 'get' to 'post' or 'put' when applicable
x = requests.post(url + '/add_new_category', headers=headers, json={
    "categoryName": "option 1"
})
read_responses.append(x)
x = requests.post(url + '/add_new_category', headers=headers, json={
    "categoryName": "option 2"
})
read_responses.append(x)
x = requests.post(url + '/add_new_category', headers=headers, json={
    "categoryName": "option 3"
})
read_responses.append(x)
x = requests.post(url + '/add_new_category', headers=headers, json={
    "categoryName": "option 4"
})
read_responses.append(x)

x = requests.post(url + '/add_new_project', headers=headers, json={
    'title': 'Spännande Grejer',
    'creator_id': 1,
    'status':  'P',
    'categories': [1, 2],
    'importance': 'Information ifyllt från CreateSuggestionPage. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ',
    'difference': 'Information ifyllt från CreateSuggestionPage. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ',
    'measurements': 'test measurements',
    'requirements': "Information ifyllt från CreateSuggestionPage. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
    'outcome': "test outcome",
    'unit': "test unit",
    "how_often": "Test how_often",
    'startTime': '2022-02-14 12:00:00',
    'deadline': '2024-04-14 12:00:00',
    

})
read_responses.append(x)

x = requests.post(url + '/add_new_project', headers=headers, json={
    'title': 'Otroliga Saker',
    'creator_id': 2,
    'status':  'D',
    'categories': [1, 2],
    'importance': 'test imp 2',
    'difference': 'test diferance 2',
    'measurements': 'test measurements 2',
    'requirements': "test Requirements 2",
    'outcome': "test outcome",
    'unit': "test unit 2",
    "how_often": "Test how_often 2",
    'startTime': '2022-03-14 12:00:00',
    'deadline': '2024-06-14 12:00:00',

})
read_responses.append(x)

x = requests.post(url + '/add_new_project', headers=headers, json={
    'title': 'test project 2',
    'creator_id': 2,
    'status':  'Utkast',
    'categories': [1, 2],
    'importance': 'test imp 2',
    'difference': 'test diferance 2',
    'measurements': None,
    'requirements': "test Requirements 2",
    'outcome': None,
    'unit': None,
    "how_often": None,
    'startTime': 'inget datum',
    'deadline': 'inget datum',

})
read_responses.append(x)

x = requests.post(url + '/add_new_project', headers=headers, json={
    'title': 'test project 3',
    'creator_id': 1,
    'status':  'Utkast',
    'categories': [1, 2],
    'importance': 'test imp 2',
    'difference': 'test diferance 2',
    'measurements': None,
    'requirements': "test Requirements 2",
    'outcome': None,
    'unit': None,
    "how_often": None,
    'startTime': 'inget datum',
    'deadline': 'inget datum',

})
read_responses.append(x)

x = requests.post(url + '/add_new_project', headers=headers, json={
    'title': 'Förbättringsarbete test',
    'creator_id': 1,
    'status':  'Utkast',
    'categories': [1, 2],
    'importance': 'test imp 2',
    'difference': 'test diferance 2',
    'measurements': None,
    'requirements': "test Requirements 2",
    'outcome': None,
    'unit': None,
    "how_often": None,
    'startTime': 'inget datum',
    'deadline': 'inget datum',

})
read_responses.append(x)

read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "Intervjua intensiven om deras upplevelse",
    "taskDescription": "Intervjua intensiven om deras upplevelse",
    'deadline': '2024-06-14 12:00:00'
}))

read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "Sammanställ resultat från X",
    "taskDescription": "lamds lsa l as sad sda",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Ongoing'
}))
read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "Sammanställ anteckningar från APT gällande X",
    "taskDescription": "task description 3",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Ongoing'
}))
read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "Intervjua Jeanette på mage & tarm",
    "taskDescription": "kasbdkanaskdnadsnsnadnsd",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Ongoing'
}))
read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "Sammanställ anteckningar från APT gällande X",
    "taskDescription": "Sammanställ anteckningar från APT gällande X",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Ongoing'
}))
read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "task6",
    "taskDescription": "Intervjua Jeanette på mage & tarm",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Finished'
}))
read_responses.append(requests.post(url + '/add_new_task/1', headers=headers, json={
    "taskName": "task7",
    "taskDescription": "Exempel uppgift Y",
    'deadline': '2024-06-14 12:00:00',
    'status': 'Finished'
}))
read_responses.append(requests.post(url + '/add_new_task/2', headers=headers, json={
    "taskName": "task1",
    "taskDescription": "Sammanställa intervjufrågor",
    'deadline': '2024-06-14 12:00:00'
}))
read_responses.append(requests.post(url + '/add_new_task/2', headers=headers, json={
    "taskName": "task2",
    "taskDescription": "task description 2",
    'deadline': '2024-06-14 12:00:00'
}))
read_responses.append(requests.post(url + '/add_new_task/2', headers=headers, json={
    "taskName": "task3",
    "taskDescription": "task description 3",
    'deadline': '2024-06-14 12:00:00'
}))


read_responses.append(requests.post(url + '/add_user_to_project/1/1', headers=headers, json={

    "role": "Team-Leader"

}))
read_responses.append(requests.post(url + '/add_user_to_project/1/2', headers=headers, json={

    "role": "Team-Member"

}))
read_responses.append(requests.post(url + '/add_user_to_project/1/4', headers=headers, json={

    "role": "Team-Member"

}))

read_responses.append(requests.post(url + '/add_user_to_project/2/2', headers=headers, json={

    "role": "Team-Leader"

}))
read_responses.append(requests.post(url + '/add_user_to_project/2/1', headers=headers, json={

    "role": "Team-Member"

}))
read_responses.append(requests.post(url + '/add_user_to_project/2/3', headers=headers, json={

    "role": "Team-Member"

}))

read_responses.append(requests.post(
    url + '/add_user_to_task/1/1', headers=headers, json={}))
read_responses.append(requests.post(
    url + '/add_user_to_task/2/1', headers=headers, json={}))
read_responses.append(requests.post(
    url + '/add_user_to_task/3/1', headers=headers, json={}))
read_responses.append(requests.post(
    url + '/add_user_to_task/8/1', headers=headers, json={}))
read_responses.append(requests.post(
    url + '/add_user_to_task/9/1', headers=headers, json={}))

############################## add below ##############################

read_responses.append(requests.post(url + '/add_new_suggestion' , headers = headers, json = {
    "title" : "test",
    "descriptionImportance" : "Importante",
    "descriptionImpact" : "Impacte",
    "descriptionRequirements" : "Requiremente",
    "status" : "Archived",
         
}))
read_responses.append(requests.post(url + '/add_new_suggestion' , headers = headers, json = {
    "title" : "test2",
    "descriptionImportance" : "123Importante",
    "descriptionImpact" : "123Impacte",
    "descriptionRequirements" : "123Requiremente",
    "status" : "Draft",
         
}))

read_responses.append(requests.put(url + "/suggestion/2" , headers = headers, json = {
    "title" : "HYPEAfterPut",
    "descriptionImportance" : "123ImportanteAfterPut",
    "descriptionImpact" : "123ImpacteAfterPut",
    "status" : "Published",
    "categories" : [{"categoryId" : 1, "categoryName" : "option 1"}] 
         
}))
read_responses.append(requests.post(url + '/add_new_suggestion' , headers = headers, json = {
    "title" : "Test Förslag",
    "descriptionImportance" : "Förbättringsförslag...",
    "descriptionImpact" : "Jag tycket att...",
    "descriptionRequirements" : "Ett glatt humör",
    "status" : "Draft",
    "categories" : [2] 
         
}))
read_responses.append(requests.post(url + '/add_new_suggestion' , headers = headers, json = {
    "title" : "Titel på ett bra försalg",
    "descriptionImportance" : "För att den är viktig",
    "descriptionImpact" : "",
    "descriptionRequirements" : "Ingenting",
    "status" : "Draft",
    "categories" : [2,3] 
         
}))

read_responses.append(requests.post(url + '/add_new_logbook' , headers = headers, json = {
    "logBookTitle": "Test1",
    "logBookDescription": "Vi vill utreda hur vi kan utföra förbättringsarbeten på ett mer effektivt vis genom att använda oss av en digital plattform. Vi har därför valt att använda oss av denna plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen. Vi har valt att använda oss av en digital plattform för att utvärdera hur vi kan förbättra arbetet på avdelningen.",
    "logBookColor":  "#96D4C9",
    "project_id": 1,
    "user": 1
         
}))

read_responses.append(requests.post(url + '/add_new_logbook' , headers = headers, json = {
    "logBookTitle": "Test2",
    "logBookDescription": "För att gå vidare med arbetet måste vi förbättra arbetsvilkoren på avdelningen. Jag föreslår att vi gör så här: 1. Vi gör så här 2. Vi gör så här 3. Vi gör så här 4. Vi gör så här 5. Vi gör så här 6. Vi gör så här 7. Vi gör så här 8. Vi gör så här 9. Vi gör så här 10. Vi gör så här 11. Vi gör så här 12. Vi gör så här 13. Vi gör så här 14. Vi gör så här 15. Vi gör så här 16. Vi gör så här 17. Vi gör så här 18. Vi gör så här 19. Vi gör så här 20. Vi gör så här 21. Vi gör så här 22. Vi gör så här 23. Vi gör så här 24. Vi gör så här 25. Vi gör så här 26. Vi gör så här 27. Vi gör så här 28. Vi gör så här 29. Vi gör så här 30. Vi gör så här 31. Vi gör så här 32. Vi gör så här 33. Vi gör så här 34. Vi gör så här 35. Vi gör så här 36. Vi gör så här 37. Vi gör så här 38. Vi gör så här 39. Vi gör så här 40. Vi gör så här 41. Vi gör så här 42. Vi gör så här 43. Vi gör så här 44. Vi gör så här 45. Vi gör så här 46. Vi gör så här 47. Vi gör så här 48. Vi gör så här 49. Vi gör så här 50. Vi gör så här 51. Vi gör så här 52. Vi gör så här 53. Vi gör så här 54. Vi gör så här 55. Vi gör så här 56. Vi gör så här 57. Vi gör så här 58. Vi gör så här 59. Vi gör så här 60. Vi gör så här 61. Vi gör så här 62. Vi gör så här 63. Vi gör så här 64. Vi gör så här 65. Vi gör så här 66. Vi gör så här 67. Vi gör så här 68. Vi gör så här 69. Vi gör så här 70. Vi gör så här 71. Vi gör så här 72.",
    "logBookColor":  "#F8A093",
    "project_id": 2,
    "user": 2
         
}))

read_responses.append(requests.post(url + '/add_new_logbook' , headers = headers, json = {
    "logBookTitle": "Test3",
    "logBookDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "logBookColor":  "#A9D7FF",
    "project_id": 1,
    "user": 1
         
}))

read_responses.append(requests.post(url + '/add_new_logbook' , headers = headers, json = {
    "logBookTitle": "Test4",
    "logBookDescription": "123abc",
    "logBookColor":  "#FFCD6C",
    "project_id": 2,
    "user": 2
         
}))

read_responses.append(requests.put(url + '/specify_users_for_task/1' , headers = headers, json = {
    "users": [1,2]
         
}))

for response in read_responses:
    if response.status_code != 200:
        print('request: ' + response.url + ' failed ' + str(response.status_code) + ' ' + response.text)

#print succes if all responses are 200
if all(response.status_code == 200 for response in read_responses):
    print('Succesfully filled database!')

