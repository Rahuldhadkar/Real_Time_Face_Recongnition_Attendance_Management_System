CREATE DATABASE faceRecognition;

USE faceRecognition;

CREATE TABLE `student` (
  `dep` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `student_id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `sec` varchar(45) DEFAULT NULL,
  `roll` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `photo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
);