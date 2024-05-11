USE tasks;
-- Item 1
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (1, 'Finish project proposal', 'Complete the project proposal document and send it to the client.', 'd1091382-e5e3-485d-a1f8-eadef8349a69', 'IN_PROGRESS', FALSE, '2023-06-30 23:59:59', '2023-05-01 10:30:00', '2023-05-15 14:20:00');

-- Item 2
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (2, 'Implement new feature', 'Add the new feature to the application based on the client''s requirements.', '6e042448-225c-4f95-8f6a-6d9f8d87e351', 'IN_PROGRESS', FALSE, '2023-07-15 17:00:00', '2023-06-01 09:00:00', '2023-06-10 11:30:00');

-- Item 3
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (3, 'Fix bug in login module', 'Investigate and fix the bug in the login module that is causing issues for users.', 'e6de6070-f231-451d-adcc-dfd561f4b7bc', 'IN_PROGRESS', FALSE, '2023-06-01 12:00:00', '2023-05-20 14:00:00', '2023-05-25 16:30:00');

-- Item 4
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (4, 'Refactor codebase', 'Refactor the codebase to improve code quality and maintainability.', '95d2b7d8-3f51-4beb-adbd-ed9082cd35ce', 'IN_PROGRESS', FALSE, '2023-08-01 23:59:59', '2023-07-01 10:00:00', '2023-07-15 14:00:00');

-- Item 5
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (5, 'Optimize database queries', 'Analyze and optimize the database queries to improve application performance.', 'f35869cd-0151-4bc4-90bc-f0e80b3ebb36', 'IN_PROGRESS', FALSE, '2023-07-31 23:59:59', '2023-06-15 11:00:00', '2023-06-30 15:30:00');

-- Item 6
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (6, 'Implement user authentication', 'Develop the user authentication system for the application.', '46663111-e679-416d-9f35-69aaf3a43bf8', 'IN_PROGRESS', FALSE, '2023-09-01 17:00:00', '2023-08-01 09:00:00', '2023-08-15 13:30:00');

-- Item 7
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (7, 'Improve UI/UX design', 'Enhance the user interface and user experience of the application.', '955669e0-5d80-4a80-b1c3-9dbc0303e29a', 'IN_PROGRESS', FALSE, '2023-10-01 23:59:59', '2023-09-01 10:00:00', '2023-09-15 14:00:00');

-- Item 8
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (8, 'Implement reporting module', 'Develop the reporting module to generate reports for the application.', '33dbb7b7-5fe6-4e36-b07e-166686341701', 'IN_PROGRESS', FALSE, '2023-11-01 17:00:00', '2023-10-01 09:00:00', '2023-10-15 13:30:00');

-- Item 9
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (9, 'Integrate with third-party API', 'Integrate the application with a third-party API to fetch additional data.', '707fd862-cea3-4a40-b016-664ebf6af419', 'IN_PROGRESS', FALSE, '2023-12-01 23:59:59', '2023-11-01 10:00:00', '2023-11-15 14:00:00');

-- Item 10
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (10, 'Implement email notification system', 'Develop the email notification system to send updates to users.', '0e5bcce9-486e-4896-ad19-9235745e8687', 'IN_PROGRESS', FALSE, '2023-08-15 17:00:00', '2023-07-20 09:00:00', '2023-08-01 11:30:00');

-- Item 11
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (11, 'Optimize application performance', 'Analyze and optimize the application''s performance to improve user experience.', '296602ad-b48f-4306-81a7-f9d388530e57', 'IN_PROGRESS', FALSE, '2023-09-30 23:59:59', '2023-09-01 10:00:00', '2023-09-20 14:00:00');

-- Item 12
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (12, 'Implement backup and recovery system', 'Develop the backup and recovery system to ensure data integrity.', 'a6c11448-8427-4689-99b3-6ef4207f17d7', 'IN_PROGRESS', FALSE, '2023-10-15 17:00:00', '2023-09-30 09:00:00', '2023-10-05 11:30:00');

-- Item 13
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (13, 'Implement user management module', 'Develop the user management module to handle user accounts and permissions.', 'dc1e6510-93b4-433d-ba05-050f3362237f', 'IN_PROGRESS', FALSE, '2023-11-01 23:59:59', '2023-10-15 10:00:00', '2023-10-25 14:00:00');

-- Item 14
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (14, 'Implement data migration process', 'Develop the data migration process to move data from the old system to the new one.', '9fedcbe5-091a-4d03-9928-f9987bc50e16', 'IN_PROGRESS', FALSE, '2023-12-01 17:00:00', '2023-11-15 09:00:00', '2023-11-25 11:30:00');

-- Item 15
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (15, 'Implement security measures', 'Develop the security measures to protect the application and its data.', '14adec1a-6377-40fb-8a86-b3e7a06c6ccb', 'IN_PROGRESS', FALSE, '2024-01-01 23:59:59', '2023-12-15 10:00:00', '2023-12-25 14:00:00');

-- Item 16
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (16, 'Implement logging and monitoring', 'Develop the logging and monitoring system to track application activities.', '160aca5c-766a-4413-b14f-37967fb15301', 'IN_PROGRESS', FALSE, '2023-11-15 17:00:00', '2023-10-30 09:00:00', '2023-11-05 11:30:00');

-- Item 17
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (17, 'Implement caching mechanism', 'Develop the caching mechanism to improve application performance.', 'a648f16e-a040-48c7-be57-f164fd8bb94a', 'IN_PROGRESS', FALSE, '2023-12-15 23:59:59', '2023-11-30 10:00:00', '2023-12-05 14:00:00');

-- Item 18
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (18, 'Implement error handling and logging', 'Develop the error handling and logging system to improve application stability.', 'd4158174-c7a1-4d97-b813-ff560da5248b', 'IN_PROGRESS', FALSE, '2024-01-01 17:00:00', '2023-12-15 09:00:00', '2023-12-25 11:30:00');

-- Item 19
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (19, 'Implement internationalization and localization', 'Develop the internationalization and localization features to support multiple languages.', '36875941-58e7-4838-b519-5cb54ad356c5', 'IN_PROGRESS', FALSE, '2024-02-01 23:59:59', '2024-01-15 10:00:00', '2024-01-25 14:00:00');

-- Item 20
INSERT INTO tasks (id, title, description, assigned_to, status, completed, due_date, create_at, update_at)
VALUES (20, 'Implement user feedback and support system', 'Develop the user feedback and support system to gather user input and provide assistance.', '98f16d4a-7a42-499c-aa4d-54b9673de253', 'IN_PROGRESS', FALSE, '2023-12-15 17:00:00', '2023-11-30 09:00:00', '2023-12-05 11:30:00');

select * from tasks