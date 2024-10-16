-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2024 at 10:57 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `das_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `attention_test_results`
--

CREATE TABLE `attention_test_results` (
  `id` int(11) NOT NULL,
  `test_type` varchar(50) DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `time_taken` float DEFAULT NULL,
  `correct_attempts` int(11) DEFAULT NULL,
  `incorrect_attempts` int(11) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attention_test_results`
--

INSERT INTO `attention_test_results` (`id`, `test_type`, `user_answer`, `correct_answer`, `result`, `time_taken`, `correct_attempts`, `incorrect_attempts`, `timestamp`) VALUES
(106, 'Attention', 'O', 'I', 'Incorrect', 986, 0, 0, '2024-10-16 18:49:35'),
(107, 'Attention', 'D', 'D', 'Correct', 4020, 1, 0, '2024-10-16 18:49:40'),
(108, 'Attention', 'X', 'X', 'Correct', 1010, 2, 0, '2024-10-16 18:49:42'),
(109, 'Attention', 'R', 'R', 'Correct', 2316, 3, 0, '2024-10-16 18:49:45'),
(110, 'Attention', 'P', 'P', 'Correct', 1950, 4, 0, '2024-10-16 18:49:48'),
(111, 'Attention', NULL, NULL, 'Correct', 15.35, 4, 1, '2024-10-16 18:49:52'),
(112, 'Attention', 'T', 'T', 'Correct', 3747, 1, -1, '2024-10-16 19:32:31'),
(113, 'Attention', 'R', 'R', 'Correct', 1988, 2, -1, '2024-10-16 19:32:34'),
(114, 'Attention', 'S', 'S', 'Correct', 1306, 3, -1, '2024-10-16 19:32:36'),
(115, 'Attention', 'V', 'V', 'Correct', 1056, 4, -1, '2024-10-16 19:32:38'),
(116, 'Attention', 'H', 'H', 'Correct', 2764, 5, -1, '2024-10-16 19:32:42'),
(117, 'Attention', NULL, NULL, 'Correct', 15.973, 5, 0, '2024-10-16 19:32:48'),
(118, 'Attention', 'L', 'L', 'Correct', 1908, 1, -1, '2024-10-16 20:44:08'),
(119, 'Attention', 'E', 'E', 'Correct', 1606, 2, -1, '2024-10-16 20:44:11'),
(120, 'Attention', 'Q', 'Q', 'Correct', 1216, 3, -1, '2024-10-16 20:44:13'),
(121, 'Attention', 'L', 'L', 'Correct', 943, 4, -1, '2024-10-16 20:44:15'),
(122, 'Attention', 'O', 'O', 'Correct', 2068, 5, -1, '2024-10-16 20:44:18'),
(123, 'Attention', NULL, NULL, 'Correct', 12.815, 5, 0, '2024-10-16 20:44:28');

-- --------------------------------------------------------

--
-- Table structure for table `memory_test_results`
--

CREATE TABLE `memory_test_results` (
  `id` int(11) NOT NULL,
  `test_type` varchar(50) DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `time_taken` float DEFAULT NULL,
  `correct_attempts` int(11) DEFAULT NULL,
  `incorrect_attempts` int(11) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `memory_test_results`
--

INSERT INTO `memory_test_results` (`id`, `test_type`, `user_answer`, `correct_answer`, `result`, `time_taken`, `correct_attempts`, `incorrect_attempts`, `timestamp`) VALUES
(13, 'Memory', '🟡🟢🔴🔵🟣', '🟡🟢🟠🔵🔴', 'Incorrect', 10.778, 0, 1, '2024-10-16 19:55:40'),
(14, 'Memory', '', 'ZCMBU', 'Incorrect', 13.053, 1, 1, '2024-10-16 19:55:55'),
(15, 'Memory', '', '77024', 'Incorrect', 8.473, 2, 1, '2024-10-16 19:56:06'),
(16, 'Memory', '', 'Green, Red, Orange, Blue, Yellow', 'Incorrect', 7.885, 2, 2, '2024-10-16 19:56:16'),
(17, 'Memory', '🟡🟢🟣🔵🔴', '🟡🟢🟣🔵🟠', 'Incorrect', 20.194, 0, 1, '2024-10-16 20:45:13'),
(18, 'Memory', '', 'CLVJE', 'Incorrect', 8.459, 1, 1, '2024-10-16 20:45:24'),
(19, 'Memory', '', '74093', 'Incorrect', 7.293, 2, 1, '2024-10-16 20:45:33'),
(20, 'Memory', '', 'Blue, Green, Yellow, Orange, Red', 'Incorrect', 20.553, 2, 2, '2024-10-16 20:45:56');

-- --------------------------------------------------------

--
-- Table structure for table `reading_test_results`
--

CREATE TABLE `reading_test_results` (
  `id` int(11) NOT NULL,
  `test_type` varchar(50) DEFAULT NULL,
  `user_answer` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  `time_taken` float DEFAULT NULL,
  `correct_attempts` int(11) DEFAULT NULL,
  `incorrect_attempts` int(11) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reading_test_results`
--

INSERT INTO `reading_test_results` (`id`, `test_type`, `user_answer`, `correct_answer`, `result`, `time_taken`, `correct_attempts`, `incorrect_attempts`, `timestamp`) VALUES
(11, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 22, 1, 0, '2024-10-16 20:35:41'),
(12, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 2, 1, 0, '2024-10-16 20:36:20'),
(13, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 17, 1, 0, '2024-10-16 20:39:26'),
(14, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 24, 2, 0, '2024-10-16 20:39:33'),
(15, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 15, 1, 0, '2024-10-16 20:39:54'),
(16, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 19, 2, 0, '2024-10-16 20:39:57'),
(17, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 13, 1, 0, '2024-10-16 20:42:01'),
(18, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 29, 1, 0, '2024-10-16 20:46:40'),
(19, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 13, 1, 0, '2024-10-16 20:49:10'),
(20, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 16, 1, 0, '2024-10-16 20:51:09'),
(21, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 2, 1, 0, '2024-10-16 20:52:10'),
(22, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 3, 1, 0, '2024-10-16 20:56:03'),
(23, 'Reading', 'The quick brown fox jumps over the lazy dog.', 'The quick brown fox jumps over the lazy dog.', 'Correct', 2, 1, 0, '2024-10-16 20:57:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attention_test_results`
--
ALTER TABLE `attention_test_results`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `memory_test_results`
--
ALTER TABLE `memory_test_results`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reading_test_results`
--
ALTER TABLE `reading_test_results`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attention_test_results`
--
ALTER TABLE `attention_test_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `memory_test_results`
--
ALTER TABLE `memory_test_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `reading_test_results`
--
ALTER TABLE `reading_test_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
