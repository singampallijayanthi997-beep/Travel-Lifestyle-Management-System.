CREATE DATABASE travel_lifestyle;

USE travel_lifestyle;

-- USERS
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(100)
);

-- LOCATIONS
CREATE TABLE Locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location_name VARCHAR(100),
    country VARCHAR(100),
    description TEXT
);

-- HOTELS
CREATE TABLE Hotels (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT,
    hotel_name VARCHAR(100),
    location_id INT,
    price_per_night INT,
    availability VARCHAR(20),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- PLACES
CREATE TABLE Places (
    place_id INT PRIMARY KEY AUTO_INCREMENT,
    place_name VARCHAR(100),
    location_id INT,
    category VARCHAR(100),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- TOURIST GUIDES
CREATE TABLE Tourist_Guides (
    guide_id INT PRIMARY KEY AUTO_INCREMENT,
    guide_name VARCHAR(100),
    phone VARCHAR(20),
    location_id INT,
    experience INT,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- TRANSPORT
CREATE TABLE Transport (
    transport_id INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(50),
    provider VARCHAR(100),
    location_id INT,
    price INT,
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- REVIEWS
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    hotel_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id)
);

-- BUDGET PLANNER
CREATE TABLE Budget_Planner (
    budget_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    location_id INT,
    total_budget INT,
    travel_days INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);