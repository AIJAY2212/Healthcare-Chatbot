-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 27, 2021 at 01:53 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2smarthealthblockdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admintb`
--

CREATE TABLE `admintb` (
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admintb`
--

INSERT INTO `admintb` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `apptb`
--

CREATE TABLE `apptb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `DoctorName` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `apptb`
--

INSERT INTO `apptb` (`id`, `UserName`, `Mobile`, `Email`, `DoctorName`, `Date`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', '2021-12-09'),
(2, 'san23', '9486365535', 'san@gmail.com', 'san', '2021-12-27');

-- --------------------------------------------------------

--
-- Table structure for table `companytb`
--

CREATE TABLE `companytb` (
  `CompanyName` varchar(250) NOT NULL,
  `RegisterNo` varchar(250) NOT NULL,
  `MobileNo` varchar(250) NOT NULL,
  `EmailId` varchar(250) NOT NULL,
  `Website` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `companytb`
--


-- --------------------------------------------------------

--
-- Table structure for table `doctortb`
--

CREATE TABLE `doctortb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Specialist` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctortb`
--

INSERT INTO `doctortb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `Specialist`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'san@gmail.com', '96003578390', 'no', 'Heart', 'san', 'san'),
('raji', 'female', '20', 'raji@gmail.com', '9486365535', 'no', 'Heart', 'raji', 'raji');

-- --------------------------------------------------------

--
-- Table structure for table `drugtb`
--

CREATE TABLE `drugtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `EmailId` varchar(250) NOT NULL,
  `DoctorName` varchar(250) NOT NULL,
  `Medicine` varchar(250) NOT NULL,
  `OtherInfo` varchar(500) NOT NULL,
  `Report` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `Hash1` varchar(250) NOT NULL,
  `Hash2` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `drugtb`
--

INSERT INTO `drugtb` (`id`, `UserName`, `Mobile`, `EmailId`, `DoctorName`, `Medicine`, `OtherInfo`, `Report`, `Date`, `Hash1`, `Hash2`) VALUES
(2, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', 'bkj', 'hgk', 'download (2).jpg', '2021-12-09', '0', '6D75351CAA1807EE59FACAF11A895DD29D9ED5C5ACC60311AA9C0DB34E01DE8D'),
(3, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', 'jgh', 'ghj', 'Jellyfish.jpg', '2021-12-09', '6D75351CAA1807EE59FACAF11A895DD29D9ED5C5ACC60311AA9C0DB34E01DE8D', 'ABBD8C57E0E8044965C28D2812A922FD7FDCE01C1322EED31853188B3D78ECC5'),
(4, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', 'jhlk', 'jhkl', 'download (1).jpg', '2021-12-09', '6D75351CAA1807EE59FACAF11A895DD29D9ED5C5ACC60311AA9C0DB34E01DE8D', '594C2508768AD948E4AD987E72273243251ED55C840E7CFE7194C5DD7D64CAB8'),
(5, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', 'dfh', 'dfhdf', 'Jellyfish.jpg', '2021-12-16', '594C2508768AD948E4AD987E72273243251ED55C840E7CFE7194C5DD7D64CAB8', 'DB38C34DC0E44FFF3954A03AE22611C3C9D58D7E08427B5C52AA97EFABC1DC68'),
(6, 'san', '9486365535', 'sangeeth5535@gmail.com', 'san', 'ghk', 'hgjk', 'Jellyfish.jpg', '2021-12-17', 'DB38C34DC0E44FFF3954A03AE22611C3C9D58D7E08427B5C52AA97EFABC1DC68', '1F056B494978EB8DCA3F571DB6DEDC356FD6FF0ABA3871E4A18BC5246979EE5C'),
(7, 'san23', '9486365535', 'san@gmail.com', 'san', 'dolo', 'health food', 'Desert.jpg', '2021-12-27', '1F056B494978EB8DCA3F571DB6DEDC356FD6FF0ABA3871E4A18BC5246979EE5C', '1BC24639A88FBDC238CEFEE22B160073DE9B815D29DF8869C97FF4E25E312F75');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no 6 trichy', 'san', 'san'),
('sanNew', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no ', 'sanNew', 'sanNew'),
('mani', 'male', '33', 'ishu@gmail.com', '9486365535', 'dgh', 'mani', 'mani'),
('san', 'male', '20', 'san@gmail.com', '9486365535', 'no 6 trichy', 'san23', 'san23');
