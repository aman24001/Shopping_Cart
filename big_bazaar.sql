-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2020 at 02:25 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopping_mall`
--

-- --------------------------------------------------------

--
-- Table structure for table `big_bazaar`
--

CREATE TABLE `big_bazaar` (
  `Product_Id` int(11) NOT NULL,
  `Product_Name` varchar(100) NOT NULL,
  `Product_Price` int(50) NOT NULL,
  `Product_Qty` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `big_bazaar`
--

INSERT INTO `big_bazaar` (`Product_Id`, `Product_Name`, `Product_Price`, `Product_Qty`) VALUES
(1, 'Shoes Men', 1200, '50'),
(2, 'T-Shirts', 700, '150'),
(3, 'Trousers', 1000, '175'),
(4, 'Leather Belts', 250, '70'),
(5, 'Perfumes', 150, '65'),
(6, 'Jackets Men', 1500, '150');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `big_bazaar`
--
ALTER TABLE `big_bazaar`
  ADD PRIMARY KEY (`Product_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `big_bazaar`
--
ALTER TABLE `big_bazaar`
  MODIFY `Product_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
