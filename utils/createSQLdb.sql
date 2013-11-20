-- phpMyAdmin SQL Dump
-- version 2.6.4-pl3
-- http://www.phpmyadmin.net
-- 
-- Host: db2536.perfora.net
-- Generation Time: Nov 20, 2013 at 01:55 PM
-- Server version: 5.1.72
-- PHP Version: 5.3.3-7+squeeze17
-- 
-- Database: `db336192140`
-- 

-- --------------------------------------------------------

-- 
-- Table structure for table `bak_devrecrods`
-- 

CREATE TABLE `bak_devrecrods` (
  `inc` int(11) NOT NULL AUTO_INCREMENT,
  `recordedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `personId` int(11) NOT NULL,
  `name` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `gender` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `race` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `birthday` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `feet` int(11) NOT NULL,
  `inches` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `hair` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `eyes` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `address` varchar(64) COLLATE latin1_general_ci NOT NULL,
  `city` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `state` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `zip` int(11) NOT NULL,
  `arrestDate` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestBy` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `agency` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `bookingDate` date NOT NULL,
  `bookingTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `charge` varchar(128) COLLATE latin1_general_ci NOT NULL,
  `charge2` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `charge3` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `bondAmt` varchar(16) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`inc`)
) ENGINE=MyISAM AUTO_INCREMENT=6083 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=6083 ;

-- --------------------------------------------------------

-- 
-- Table structure for table `bak_records`
-- 

CREATE TABLE `bak_records` (
  `inc` int(11) NOT NULL AUTO_INCREMENT,
  `recordedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `personId` int(11) NOT NULL,
  `name` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `gender` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `race` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `birthday` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `feet` int(11) NOT NULL,
  `inches` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `hair` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `eyes` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `address` varchar(64) COLLATE latin1_general_ci NOT NULL,
  `city` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `state` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `zip` int(11) NOT NULL,
  `arrestDate` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestBy` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `agency` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `bookingDate` date NOT NULL,
  `bookingTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `charge` varchar(128) COLLATE latin1_general_ci NOT NULL,
  `charge2` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `charge3` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `bondAmt` varchar(16) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`inc`)
) ENGINE=MyISAM AUTO_INCREMENT=5822 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=5822 ;

-- --------------------------------------------------------

-- 
-- Table structure for table `devlatestPersonId`
-- 

CREATE TABLE `devlatestPersonId` (
  `id` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

-- 
-- Table structure for table `devrecords`
-- 

CREATE TABLE `devrecords` (
  `inc` int(11) NOT NULL AUTO_INCREMENT,
  `recordedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `personId` int(11) NOT NULL,
  `mugshotHash` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `name` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `gender` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `race` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `birthday` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `feet` int(11) NOT NULL,
  `inches` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `hair` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `eyes` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `address` varchar(64) COLLATE latin1_general_ci NOT NULL,
  `city` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `state` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `zip` int(11) NOT NULL,
  `arrestDate` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestBy` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `agency` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `bookingDate` date NOT NULL,
  `bookingTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `charge` varchar(128) COLLATE latin1_general_ci NOT NULL,
  `charge2` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `charge3` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `bondAmt` varchar(16) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`inc`),
  UNIQUE KEY `personId` (`personId`)
) ENGINE=MyISAM AUTO_INCREMENT=25549 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=25549 ;

-- --------------------------------------------------------

-- 
-- Table structure for table `latestPersonId`
-- 

CREATE TABLE `latestPersonId` (
  `id` int(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- --------------------------------------------------------

-- 
-- Table structure for table `records`
-- 

CREATE TABLE `records` (
  `inc` int(11) NOT NULL AUTO_INCREMENT,
  `recordedOn` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `personId` int(11) NOT NULL,
  `name` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `gender` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `race` varchar(8) COLLATE latin1_general_ci NOT NULL,
  `birthday` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `feet` int(11) NOT NULL,
  `inches` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `hair` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `eyes` varchar(16) COLLATE latin1_general_ci NOT NULL,
  `address` varchar(64) COLLATE latin1_general_ci NOT NULL,
  `city` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `state` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `zip` int(11) NOT NULL,
  `arrestDate` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `arrestBy` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `agency` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `bookingDate` date NOT NULL,
  `bookingTime` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `charge` varchar(128) COLLATE latin1_general_ci NOT NULL,
  `charge2` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `charge3` varchar(128) COLLATE latin1_general_ci DEFAULT NULL,
  `bondAmt` varchar(16) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`inc`),
  UNIQUE KEY `personId` (`personId`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

-- 
-- Table structure for table `users`
-- 

CREATE TABLE `users` (
  `username` varchar(32) COLLATE latin1_general_ci NOT NULL,
  `password` varchar(32) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

