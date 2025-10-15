# Fetching and Displaying User Data from an API

You are creating a simple profile page that fetches user data from an API:  
 **[https://jsonplaceholder.typicode.com/users/1](https://jsonplaceholder.typicode.com/users/1)**

---

##  Objective
Fetch and display the **user’s name** and **email** on a webpage.

---

## Approach

To get user data from the API, we use the **`fetch()`** function, which sends a network request and returns a promise.

### Steps:
1. **Use `fetch()`** to call the API.  
2. **Convert** the response to JSON using `.json()`.  
3. **Access** the required data fields (`name` and `email`).  
4. **Display** them dynamically in the webpage.

---
#  Handling Loading and Error States

When fetching data from an API, it’s important to provide **feedback** to users so they know what’s happening — whether data is **loading**, has **loaded successfully**, or an **error** has occurred.

---

##  Loading State

Before the data arrives, display a message such as:

> “Loading user data...”

### Why:
- Keeps users informed that the app is working.  
- Improves user experience by preventing confusion or impatience.  

### How:
- Show this message immediately **before** making the fetch request.  
- Once the data successfully loads, **remove** or replace the message with the fetched content.



