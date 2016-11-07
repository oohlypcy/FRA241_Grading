-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 01, 2016 at 08:16 PM
-- Server version: 5.7.11-0ubuntu6
-- PHP Version: 7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;

/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2016FRA241G2`
--

-- --------------------------------------------------------

--
-- Table structure for table `Enrol`
--

CREATE TABLE `Enrol` (
  `ID` bigint(11) NOT NULL,
  `Subject_ID` varchar(45) NOT NULL,
  `subject_Year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Enrol`
--

INSERT INTO `Enrol` (`ID`, `Subject_ID`, `subject_Year`) VALUES
(58340500017, 'FRA222', 59);

-- --------------------------------------------------------

--
-- Table structure for table `Group`
--

CREATE TABLE `Group` (
  `Subject_ID` varchar(45) NOT NULL,
  `Year` int(11) NOT NULL,
  `WorkID` int(11) NOT NULL,
  `ID` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `media`
--

CREATE TABLE `media` (
  `Subject_ID` varchar(45) NOT NULL,
  `Year` int(11) NOT NULL,
  `File_name` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `ID` bigint(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `Subject_ID` varchar(45) NOT NULL,
  `Year` int(11) NOT NULL,
  `Description` varchar(45) DEFAULT NULL,
  `FullMark` int(11) DEFAULT NULL,
  `Grading` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`Subject_ID`, `Year`, `Description`, `FullMark`, `Grading`) VALUES
('FRA222', 59, NULL, 100, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SubmitWork`
--

CREATE TABLE `SubmitWork` (
  `Subject_ID` varchar(45) NOT NULL,
  `Year` int(11) NOT NULL,
  `WorkID` int(11) NOT NULL,
  `ID` bigint(20) NOT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  `Mark` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `ID` bigint(20) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Title` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Surname` varchar(45) DEFAULT NULL,
  `E-mail` varchar(45) DEFAULT NULL,
  `Role` varchar(45) DEFAULT NULL,
  `Faculty` varchar(45) DEFAULT NULL,
  `Major` varchar(45) DEFAULT NULL,
  `Enro-Yearl` varchar(45) DEFAULT NULL,
  `Picture` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`ID`, `Password`, `Title`, `Name`, `Surname`, `E-mail`, `Role`, `Faculty`, `Major`, `Enro-Yearl`, `Picture`) VALUES
(58340500017, 'Boomming1*', 'Mr.', 'Chaiyaporn', 'Boonyasathian', 'chaiya45689@gmail.com', 'student', 'FIBO', 'robotic and automation', '58', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `work`
--

CREATE TABLE `work` (
  `Subject_ID` varchar(45) NOT NULL,
  `Year` int(11) NOT NULL,
  `WorkID` int(11) NOT NULL,
  `Deadlines` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `FullMark` varchar(45) DEFAULT NULL,
  `Grading` varchar(45) DEFAULT NULL,
  `lim_member` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `work`
--

INSERT INTO `work` (`Subject_ID`, `Year`, `WorkID`, `Deadlines`, `status`, `type`, `FullMark`, `Grading`, `lim_member`) VALUES
('FRA222', 59, 1, NULL, NULL, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Enrol`
--
ALTER TABLE `Enrol`
  ADD PRIMARY KEY (`ID`,`Subject_ID`,`subject_Year`),
  ADD KEY `fk_Enrol_User1_idx` (`ID`),
  ADD KEY `fk_Enrol_subject1_idx` (`Subject_ID`,`subject_Year`);

--
-- Indexes for table `Group`
--
ALTER TABLE `Group`
  ADD PRIMARY KEY (`Subject_ID`,`Year`,`WorkID`);

--
-- Indexes for table `media`
--
ALTER TABLE `media`
  ADD PRIMARY KEY (`Subject_ID`,`Year`),
  ADD KEY `fk_media_subject1_idx` (`Subject_ID`,`Year`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`Subject_ID`,`Year`);

--
-- Indexes for table `SubmitWork`
--
ALTER TABLE `SubmitWork`
  ADD PRIMARY KEY (`Subject_ID`,`Year`,`WorkID`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `work`
--
ALTER TABLE `work`
  ADD PRIMARY KEY (`Subject_ID`,`Year`,`WorkID`),
  ADD KEY `fk_work_subject1_idx` (`Subject_ID`,`Year`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Enrol`
--
ALTER TABLE `Enrol`
  ADD CONSTRAINT `fk_Enrol_User1` FOREIGN KEY (`ID`) REFERENCES `User` (`ID`),
  ADD CONSTRAINT `fk_Enrol_subject1` FOREIGN KEY (`Subject_ID`,`subject_Year`) REFERENCES `subject` (`Subject_ID`, `Year`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Group`
--
ALTER TABLE `Group`
  ADD CONSTRAINT `fk_Group_work1` FOREIGN KEY (`Subject_ID`,`Year`,`WorkID`) REFERENCES `work` (`Subject_ID`, `Year`, `WorkID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `media`
--
ALTER TABLE `media`
  ADD CONSTRAINT `fk_media_subject1` FOREIGN KEY (`Subject_ID`,`Year`) REFERENCES `subject` (`Subject_ID`, `Year`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `SubmitWork`
--
ALTER TABLE `SubmitWork`
  ADD CONSTRAINT `fk_SubmitWork_work1` FOREIGN KEY (`Subject_ID`,`Year`,`WorkID`) REFERENCES `work` (`Subject_ID`, `Year`, `WorkID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `work`
--
ALTER TABLE `work`
  ADD CONSTRAINT `fk_work_subject1` FOREIGN KEY (`Subject_ID`,`Year`) REFERENCES `subject` (`Subject_ID`, `Year`) ON DELETE NO ACTION ON UPDATE NO ACTION;


