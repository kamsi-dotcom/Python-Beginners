''' Task 1: List Operations
- **Description**: Create a list of your favorite fruits (at least 5). Write code to:
  1. Add a new fruit to the end of the list.
  2. Remove the third fruit from the list.
  3. Replace the second fruit with another fruit.
  4. Print the final list.'''
#CODE
#1
# my_list=['apple','pineapple','mango','pear','banana']
# my_list.append('watermelon')
# my_list.remove('mango')
# my_list[1]='lemon'
# print(my_list)


''' Task 2: Tuple Basics
- **Description**: Create a tuple that contains the names of 4 cities you would like to visit. Write code to:
  1. Print the first city in the tuple.
  2. Print the last city in the tuple.
  3. Try to change the second city (this will result in an error, demonstrating tuple immutability).'''
# CODE
# my_tuple=('Toronto','Mumbia','Abuja','Liverpool')
# print(my_tuple[0])
# print(my_tuple[3])
# my_tuple[1]='Miami'


''' Task 3: Dictionary Manipulation
- **Description**: Create a dictionary with the following key-value pairs:
  ```python
  person = {
      "name": "John",
      "age": 25,
      "city": "New York"
  }
  ```
  Write code to:
  1. Add a new key-value pair for "email".
  2. Update the "age" to 26.
  3. Remove the "city" key from the dictionary.
  4. Print the final dictionary.'''
# CODE
# person={'name': 'John',
#         'age': 25,
#         'city':'New York'
#         }
# person['email']='ezekamsi190@gmail.com'
# person['age']=26
# person.pop('city')
# print(person)

''' Task 4: Nested Dictionary Access
- **Description**: Create a dictionary that represents a student's profile with the following nested structure:
  ```python
  student_profile = {
      "name": "Alice",
      "age": 21,
      "grades": {
          "math": 90,
          "science": 85,
          "literature": 88
      },
      "contact_info": {
          "email": "alice@example.com",
          "phone": "123-456-7890"
      }
  }
  ```
  Write code to:
  1. Print the student's name.
  2. Access and print the student's science grade.
  3. Update the literature grade to 92.
  4. Add a new key-value pair in the `contact_info` for "address" with any value.
  5. Print the updated dictionary.'''
# CODE
student_profile = {
      "name": "Alice",
      "age": 21,
      "grades": {
          "math": 90,
          "science": 85,
          "literature": 88
      },
      "contact_info": {
          "email": "alice@example.com",
          "phone": "123-456-7890"
      }
  }
# print(student_profile['name'])
# print(student_profile['grades']['science'])
# student_profile['grades']['literature']=92
# print(student_profile['grades']['literature'])
# student_profile['contact_info']['address']='21 ,Akowonjo Road'
# print(student_profile['contact_info']['address'])
''' Task 5: Multi-level Nested Dictionary
- **Description**: Create a dictionary that represents a company with departments and their respective managers and employees:
  ```python
  company = {
      "IT": {
          "manager": "John Doe",
          "employees": ["Alice", "Bob", "Charlie"]
      },
      "HR": {
          "manager": "Jane Smith",
          "employees": ["Dave", "Eva"]
      },
      "Marketing": {
          "manager": "Michael Brown",
          "employees": ["Fiona", "George"]
      }
  }
  ```
  Write code to:
  1. Print the name of the HR manager.
  2. Access and print the list of employees in the IT department.
  3. Add a new employee to the Marketing department.
  4. Change the manager of the IT department to "Sarah Connor".
  5. Print the updated dictionary.'''
# CODE
company = {
      "IT": {
          "manager": "John Doe",
          "employees": ["Alice", "Bob", "Charlie"]
      },
      "HR": {
          "manager": "Jane Smith",
          "employees": ["Dave", "Eva"]
      },
      "Marketing": {
          "manager": "Michael Brown",
          "employees": ["Fiona", "George"]
      }
  }
# print(company['HR']['manager'])
# print(company['IT']['employees'])
company['Marketing']['employees']=['Fiona','George','Michael']
# company['IT']['manager']="Sarah Connor"
# print(company['Marketing']['employees'])
# print(company['IT']['manager'])


