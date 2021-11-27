-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 27, 2021 lúc 11:44 AM
-- Phiên bản máy phục vụ: 10.4.21-MariaDB
-- Phiên bản PHP: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `blog1`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `blog_user`
--

CREATE TABLE `blog_user` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `create_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `blog_user`
--

INSERT INTO `blog_user` (`id`, `title`, `content`, `create_date`) VALUES
(1, 'đsfdfg', '', '2021-11-27 16:18:05'),
(2, 'gdfgf', 'ưereytrdut', '2021-11-27 16:19:17'),
(3, 'treytu', 'sẻtyujhikjdfvbghj', '2021-11-27 16:21:44'),
(4, 'treytu', 'sẻtyujhikjdfvbghj', '2021-11-27 16:22:19'),
(5, 'treytu', 'sẻtyujhikjdfvbghj', '2021-11-27 16:23:24'),
(6, '678', '567', '2021-11-27 16:24:16'),
(7, '5', '5', '2021-11-27 16:25:02'),
(8, 'rtyu', 'tyu', '2021-11-27 16:27:03'),
(9, '67ui', '567', '2021-11-27 16:31:34'),
(10, 'sdfg', 'dfgh', '2021-11-27 16:34:46');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `blog_user`
--
ALTER TABLE `blog_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `blog_user`
--
ALTER TABLE `blog_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
