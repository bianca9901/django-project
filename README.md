# The Django Restaurant

![Logo](documentation/about/logo.png)

## About

#### Django is a fictional restaurant that not only offers delicious food but also engaging events for its users to partake in.

**Django Restaurant Main Features:**

* **Event reservations:** Explore upcoming events on the 'Events' page and choose the ones that best match your interests and secure your spot with ease.

* **Easy reservation process:** The intuitive reservation process allows you to pick your desired event, select the number of spots you need, and make a reservation for yourself and your companions.

* **Personalized Events dashboard:** Keep track of your upcoming plans effortlessly with the 'My Events' page. Here, you can find all the details you need. Need to change your plans? No problem, do it directly from your dashboard.

* **Menu exploration:** Explore the 'Menu' page to see the drinks and dishes served. The Menu goes by the admin dashboard so the staff will always update the page with the latest drinks and foods for you to see.

* **Share your experience:** Your feedback is valuable! You can always leave a review to share your thoughts and help us improve. Don’t worry if you want to edit or delete your review(s) later, you can always access and manage them.

---

## User Stories

### Menu

* As a **site user,** I want to discover the menu so that I can decide what dishes to try in advance.

* As an **admin,** I want to add, update, and delete menu items so that I can easily inform guests about their options.


### Events 
* As a **site user,** I want to see the offered events so that I can learn more and potentially attend.

* As a **site user,** I want to make reservations for events so that I can secure my spot.

* As a **site user,** I want to stay updated about new events so that I can explore new ones that interest me.

* As a **site user,** I want to manage my event bookings on the website so that I don’t need to contact the restaurant.

* As a **site user,** I want to know if there has been an decrease in the available spots for an event I am attending so that I know how many people there will be.

* As an **admin,** I want to add, update, and delete events so that I can easily inform guests about their options.

* As an **admin,** I want to see guest reservations from the dashboard so that I can easily prepare staff for the event demand.

* As an **admin,** I want to create, read, update, and delete restaurant reservations made by users so that I can update the website if calls or emails have been made that need to be reflected on the website.

### Reviews

* As a **site user,** I want to read others reviews so that I can get honest opinions about the restaurant.

* As a **site user,** I want to leave a review so that I can inform others.

* As a **site user,** I want to delete or edit my reviews so that I can adjust my feedback based on evolving experiences.

* As an **admin,** I want to manage reviews from the dashboard so that inappropriate reviews do not stay on the website.

### General

* As a **site user,** I want to see imagery of the restaurant so that I can get a visual feel.

* As a **site user,** I want to find the restaurant's location so that I know where to go.

* As a **site user,** I want to learn more about the restaurant's staff so that I know who they are.

* As a **site user,** I want to find the restaurant's contact information so that I can contact them.

---

## Features

### Home Page

**Presents the restaurant's offerings through text and image slides.**

![Home](documentation/pages/home.png)

### About Us Page

**Displays images of staff and text about the restaurant's philosophy.**

![About Us](documentation/pages/about-us.png)

### Menu Page

**Displays food and drink offerings with descriptions and prices.**

![Menu](documentation/pages/menu.png)

### Events Page

**Displays upcoming events with date, time, description, and the available spots left.**

![Events](documentation/pages/events.png)

### Event Reservation Page

**Displays a concise recap about the selected event, a number box for users to specify the number of companions, and a submit button.**

![Events](documentation/pages/reservation-form.png)

### My Events Page
**Shows authenticated users their upcoming events and cancelation and editing buttons.**

![My Events](documentation/pages/my-events.png)

### Reviews Page
**Displays all guest reviews.**

![Reviews](documentation/pages/reviews.png)

### Review Form
**Displays textbox that allows users to write and submit their reviews.**

![Review form](documentation/pages/review-form.png)

### Edit Review Form
**Displays prepopulated textbox with previously written review text.**

![Edit review](documentation/pages/edit-review-form.png)

---

## Design

### The design choice:
I aimed to give the restaurant website a modern and sleek style, which drove my font and background color choices, that is grey, off-white, white, and gold.

With the modern feel as the base, I also wanted to give the restaurant a warm, and joyful ambiance. Therefore, the images were carefully selected to create an atmosphere that aligns with the restaurant's philosophy and key features.

When it comes to the messages and buttons, I wanted them to catch the eye. That's why I opted for attention-grabbing colors that also align with its purpose, yellow for info, etc.

Typography played a vital role to give the right feel. I aimed for a cool and hip style that resonates with the targeted audience.

As for the logo and the signed "-Django Team" text pieces, I aspired to select a Google font that portrays a handwritten style, adding a personal touch.

### Colors used:
**For the overall design I used grey, off-white, white, and gold:**

RGB(110, 117, 124)

![Grey](documentation/design/grey.png)

RGB(248, 248, 248)

![Off White](documentation/design/offwhite.png)

RGB(255, 255, 255)

![White](documentation/design/white.png)

RGB(190, 194, 133)

![Gold](documentation/design/gold.png)


**For messages and buttons I used 2 nuances of red, 2 nuances of green, and yellow:**

RGB(209, 77, 70)

![Red1](documentation/design/red-nyance1.png)

RGB(203, 68, 74)

![Red2](documentation/design/red-nyance2.png)

RGB(116, 197, 120)

![Green1](documentation/design/green-nyance1.png)

RGB(169, 235, 176)

![Green2](documentation/design/green-nyance2.png)

RGB(255, 255, 132)

![Yellow](documentation/design/yellow.png)


### Typography: 

**I used [Google Fonts](https://fonts.google.com/) for all text:**

For the logo and the signed "-Django Team" text pieces I used Zeyada Regular 400.
![Zeyada](documentation/design/zeyada.png)

For the navbar and headlines, I used Caveat Bold 700.
![Caveat](documentation/design/caveat.png)

For the paragraphs, I used Open Sans Medium 500 Italic.
![Open Sans](documentation/design/opensans.png)

---

## Testing

Please visit [this link](TESTING.md) to find test-related documentation.

---

## Deployment

Please visit [this link](DEPLOYMENT.md) to find deployment-related documentation.

---

## Data Schema

### The application `app_restaurant` has four models that represent different aspects of the restaurant.

**`restaurant_event:`**

The `restaurant_event` model represents events hosted by the restaurant.

Fields:
- `name`: The name of the event.
- `event_date`: The date and time of the event.
- `description`: A text field describing the event.
- `available_spots`: The number of available spots for the event.
- `image`: An image associated with the event.

Methods:
- `calculate_available_spots`: Calculates the number of available spots for the event by considering the reserved spots from related reservations.

| Name                 | Database Key       | Field Type         | Validation                                                                               |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------------------------------------------------- |
| name                 | name               | CharField          | max_length=100, verbose_name='Event Name'                                                |
| event_date           | event_date         | DateTimeField      | verbose_name='Event Date'                                                                |
| description          | description        | TextField          | blank=True, verbose_name='Event Description'                                             |
| available_spots      | available_spots    | PositiveIntegerField | default=30, verbose_name='Available Spots'                                             |
| image                | image              | ImageField         | blank=True, verbose_name='Image'                                                         |
| calculate_available_spots | calculate_available_spots | Property      | Calculates available spots considering existing reservations                      |
---

**`restaurant_reservation`**

The `restaurant_reservation` model represents reservations made by users for restaurant events.

Fields:
* `number_of_friends`: The number of friends accompanying the user.
* `event`: A foreign key to the associated event.
* `user`: A foreign key to the user making the reservation.


| Name                 | Database Key       | Field Type         | Validation                                                                               |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------------------------------------------------- |
| number_of_friends    | number_of_friends  | PositiveIntegerField | default=0, validators=[MaxValueValidator(30)]                                          |
| event                | event              | ForeignKey         | to='restaurant_event', on_delete=models.CASCADE, related_name='reservations'             |
| user                 | user               | ForeignKey         | to=User, on_delete=models.CASCADE                                                        |
---

**`menu`**

The `menu` model represents items available in the restaurant's menu.

Fields:
* `name`: The name of the menu item.
* `description`: A text field describing the item.
* `price`: The price of the item.
* `category`: The category of the item (food or drinks).


| Name                 | Database Key       | Field Type         | Validation                                                                               |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------------------------------------------------- |
| name                 | name               | CharField          | max_length=100, verbose_name='Item Name'                                                 |
| description          | description        | TextField          | blank=True, verbose_name='Item Description'                                              |
| price                | price              | DecimalField       | max_digits=10, decimal_places=2                                                          |
| category             | category           | CharField          | max_length=10, choices=CATEGORY_CHOICES, default=FOOD, verbose_name='Item Category'      |
---

**`review`**

The `review` model represents user reviews for the restaurant.

Fields:
* `user`: A foreign key to the user who wrote the review.
* `review_text`: The text of the review.
* `pub_date`: The date and time when the review was published.

| Name                 | Database Key       | Field Type         | Validation                                                                               |
| -------------------- | ------------------ | ------------------ | ---------------------------------------------------------------------------------------- |
| user                 | user               | ForeignKey         | to=User, on_delete=models.CASCADE                                                        |
| review_text          | review_text        | TextField          | blank=False                                                                              |
| pub_date             | pub_date           | DateTimeField      | auto_now_add=True                                                                        |
---

### models.py

![model1 database schema](documentation/data-schema/model-table1.png)
![model2 database schema](documentation/data-schema/model-table2.png)

---

## Bugs

### Solved Bugs

**Bootstrap Modal Issue:** I wanted to use a modal for defensive programming. I Googled Bootstrap modals, and without thinking much more about it. I used the syntax provided in the Bootstrap documentation. I then tested my website but the modal would not pop up, causing a lot of confusion.

**Solution:** After doing some research I found [this](https://stackoverflow.com/questions/17142790/bootstrap-modal-not-working-at-all) question from someone encountering the same issue as I, asking for help. And someone had an answer that I figured could be the issue.

![Answer](documentation/bugs/stackoverflow.png)

The issue stemmed from the fact that I used Bootstrap 5 in my base.html and when I initially Googled Bootstrap modals unfortunately the first result was the documentation for Bootstrap 4 which was the syntax I was trying to use in my code. This syntax did indeed not have the **bs** attribute as mentioned in the Stack Overflow answer.

It was my fault that I had not checked the version of the modal. The good news is that
when I changed to v.5 for the modal documentation in Bootstrap, (the version of Bootstrap that I used in my base.html) The modal would work as expected.

This situation served as a valuable lesson in staying up-to-date with framework changes.


### Unsolved Bugs
**Edit Reservation Issue:** I encountered an unresolved bug related to the Reservation feature, and I'd like to share my experience with it. Unfortunately, due to time constraints during the project, I wasn't able to fully implement all aspects of CRUD functionality in this area.

The specific issue is the process of editing reservations. The original intention was for the reservation edit form to be prepopulated with the user's existing reservation details. This included accounting for the number of spots reserved and making sure they were correctly updated in the available spots count. For instance, if there were initially 10 available spots and a user reserved 5 spots, there should have been 5 spots remaining. If the user then attempted to edit their reservation by increasing the number of spots, the intention was to restore the originally reserved spots to the available count (so that it's back to 10 in this example).
This step was crucial to ensure a proper user experience. For instance, if a user had initially booked 5 spots but then decided to edit the reservation to increase the number of spots to 6, without restoring their originally reserved spots, the system would incorrectly show the event as fully booked even though there were spots available.

Despite multiple days attempting, I struggled to accurately incorporate this aspect of CRUD functionality. The challenge stemmed from various factors, including potential changes in the available spots due to other users reserving spots in the same event, making it difficult to track and manage the correct spot count for editing reservations.

Now, I had to make a tough decision. The only solution left was to cancel a user's existing reservation and guide them back to the event reservation form, where they could see the updated available spots count and make a new booking. While this solution is not ideal, I made sure to include clear and important messages throughout the edit reservation process to guide users and provide them with the best experience possible.

I feel deeply disappointed that I couldn't fully address this issue within the given timeframe.

---

## Features left to implement

* Implement the "U" in CRUD for reservations, as mentioned in the bugs section [here](#unsolved-bugs).

* Allow authenticated users to filter the "Reviews" page to see their previous reviews.

* Implement pagination for the "Events" and "Reviews" pages.

* Ensure consistent image sizes on the "Events" page to enhance UX.

* Add a Favicon

----

## Technologies Used

### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): was used for structuring the website's content.

* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): was used to style the website.

* [Python](https://www.python.org/): was used for the logic.

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): was used to disable a button.

### Frameworks and Libraries

* [Django](https://www.djangoproject.com/): was used for building the web application.

* [Bootstrap](https://getbootstrap.com/): was used for responsive design and layout.

### Databases

* [SQLite](https://www.sqlite.org/index.html): was used as a development database.

* [PostgreSQL](https://www.postgresql.org/): was the database used to store all the data.

## Other Technologies
* [Cloudinary](https://cloudinary.com/): was used for efficient image management and delivery.

* [Github](https://github.com/): was used for repository hosting and version control.

* [Git](https://git-scm.com/): was used for version control.

* [GitPod](gitpod.io): was used for writing and editing code.

* [Heroku](https://id.heroku.com/login): was used to deploy the project.

* [Pip3](https://pypi.org/project/pip/): was the package manager used to install the dependencies.

* [Gunicorn](https://gunicorn.org/): was the web server used to run the website.

* [Psycopg](https://pypi.org/project/psycopg2/): was used as the database adapter for Python.

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/): was used for authentication, registration, and account management.

* [Pillow](https://pypi.org/project/Pillow/): was used for image processing.

* [Google Fonts](https://fonts.google.com/): was used for the typography.

* [Font Awesome](https://fontawesome.com): was used for the social media icons.

---

## Credits

### Inspiration and Help:

 [These](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) Youtube videos served as a helper to get started with my event views and the application for members.

 [This](https://www.youtube.com/@technologyit5133) Youtube channel showed me general tips and tricks about Django that I applied.

 [This](https://stackoverflow.com/questions/17142790/bootstrap-modal-not-working-at-all) question in Stack Overflow helped me overcome the issue I had with Bootstrap.

 [This](https://github.com/IuliiaKonovalova/e-commerce/blob/main/DEPLOYMENT.md) documentation was used as a template for my DEPLOYMENT.md.

### Media:

All images were sourced from [Pexels](https://www.pexels.com).

**Carousel Images:**

* [Bar Image](https://www.pexels.com/photo/person-pouring-wine-in-a-jigger-making-a-cocktail-drink-15081737/)

* [Food Image](https://www.pexels.com/sv-se/foto/mat-restaurang-hander-manniskor-1310777/)

* [Restaurant Interior Image](https://www.pexels.com/photo/empty-dining-sets-at-the-eatery-2313037/)

* [Friends Image](https://www.pexels.com/photo/friends-drinking-whisky-and-cocktails-in-a-bar-16374147/)

* [Man playing guitar Image](https://www.pexels.com/photo/photo-of-man-playing-guitar-4054461/)

**About Us Image:**

* [Group photo image](https://www.pexels.com/sv-se/foto/manniskor-kvinna-vanner-man-6150584/)

**Events Images:**

* [Chess image](https://www.pexels.com/photo/men-playing-chess-on-the-wooden-table-11434528/)

* [Karaoki image](https://www.pexels.com/photo/man-singing-1238943/)

* [Billiard image](https://www.pexels.com/photo/people-playing-billiard-5055267/)

* [Monopoly](https://www.pexels.com/photo/game-figures-on-board-on-table-17391987/)

* [Beerpong](https://www.pexels.com/photo/photograph-of-women-playing-beer-pong-7022149/)

* [Singer](https://www.pexels.com/photo/woman-playing-electric-guitar-1864653/)

### Content:

[This](https://www.coastlinenservices.com/blog/vegetarian-and-vegan-menu-options/) blog is where the menus' food titles were taken from. 

---