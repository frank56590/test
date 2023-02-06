/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : srcededb

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2022-03-17 11:32:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for acceso
-- ----------------------------
DROP TABLE IF EXISTS `acceso`;
CREATE TABLE `acceso` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(32) DEFAULT NULL,
  `clave` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of acceso
-- ----------------------------
INSERT INTO `acceso` VALUES ('1', 'admin', 'admin');

-- ----------------------------
-- Table structure for carreras
-- ----------------------------
DROP TABLE IF EXISTS `carreras`;
CREATE TABLE `carreras` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(32) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `titulo` (`titulo`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of carreras
-- ----------------------------
INSERT INTO `carreras` VALUES ('1', 'Administracion');
INSERT INTO `carreras` VALUES ('2', 'Agroalimentaria');
INSERT INTO `carreras` VALUES ('3', 'Contaduria');
INSERT INTO `carreras` VALUES ('4', 'Distribucion de alimentos');
INSERT INTO `carreras` VALUES ('5', 'Educacion fisica');
INSERT INTO `carreras` VALUES ('6', 'Educacion inicial');
INSERT INTO `carreras` VALUES ('7', 'Educacion integral');
INSERT INTO `carreras` VALUES ('8', 'Enfermeria');
INSERT INTO `carreras` VALUES ('9', 'Fisioterapia');
INSERT INTO `carreras` VALUES ('10', 'Informatica');
INSERT INTO `carreras` VALUES ('11', 'Terapia ocupacional');
INSERT INTO `carreras` VALUES ('12', 'Turismo');
INSERT INTO `carreras` VALUES ('13', 'Veterinaria');

-- ----------------------------
-- Table structure for docentes
-- ----------------------------
DROP TABLE IF EXISTS `docentes`;
CREATE TABLE `docentes` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(32) DEFAULT '',
  `apellido` varchar(32) DEFAULT '',
  `cedula` varchar(8) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of docentes
-- ----------------------------
INSERT INTO `docentes` VALUES ('1', 'Ramon', 'Lozada', '27802134');
INSERT INTO `docentes` VALUES ('5', 'Jesus', 'Lozada', '8953714');

-- ----------------------------
-- Table structure for unidades
-- ----------------------------
DROP TABLE IF EXISTS `unidades`;
CREATE TABLE `unidades` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `id_docente` int(255) NOT NULL,
  `unidad` varchar(32) DEFAULT NULL,
  `carrera` varchar(255) DEFAULT '',
  `dias` varchar(12) DEFAULT NULL,
  `horario_l_in` varchar(7) DEFAULT '--',
  `horario_l_out` varchar(7) DEFAULT '--',
  `horario_ma_in` varchar(7) DEFAULT '--',
  `horario_ma_out` varchar(7) DEFAULT '--',
  `horario_mi_in` varchar(7) DEFAULT '--',
  `horario_mi_out` varchar(7) DEFAULT '--',
  `horario_j_in` varchar(7) DEFAULT '--',
  `horario_j_out` varchar(7) DEFAULT '--',
  `horario_v_in` varchar(7) DEFAULT '--',
  `horario_v_out` varchar(7) DEFAULT '--',
  PRIMARY KEY (`id`,`id_docente`),
  KEY `relacion_cerrara_unidad` (`carrera`),
  KEY `relacion_docente_unidad` (`id_docente`),
  CONSTRAINT `relacion_cerrara_unidad` FOREIGN KEY (`carrera`) REFERENCES `carreras` (`titulo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `relacion_docente_unidad` FOREIGN KEY (`id_docente`) REFERENCES `docentes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of unidades
-- ----------------------------
INSERT INTO `unidades` VALUES ('7', '1', 'Warao', 'Informatica', 'V', '--', '--', '--', '--', '--', '--', '--', '--', '10:30', '00:30');
INSERT INTO `unidades` VALUES ('8', '1', 'Redes', 'Informatica', 'J', '--', '--', '--', '--', '--', '--', '10:30', '00:30', '--', '--');
INSERT INTO `unidades` VALUES ('9', '1', 'Programacion I', 'Informatica', 'MI-V', '--', '--', '--', '--', '10:30', '00:30', '--', '--', '22:30', '13:30');
INSERT INTO `unidades` VALUES ('11', '5', 'Prueba', 'Fisioterapia', 'L', '21:03', '21:02', '--', '--', '--', '--', '--', '--', '--', '--');
INSERT INTO `unidades` VALUES ('12', '5', 'Warao', 'Distribucion de alimentos', 'MI', '--', '--', '--', '--', '10:20', '13:00', '--', '--', '--', '--');
INSERT INTO `unidades` VALUES ('13', '5', 'Warao', 'Agroalimentaria', 'MA', '--', '--', '22:49', '21:54', '--', '--', '--', '--', '--', '--');
INSERT INTO `unidades` VALUES ('14', '1', 'Introduccion a las tips', 'Informatica', 'MA', '--', '--', '01:28', '01:25', '--', '--', '--', '--', '--', '--');
INSERT INTO `unidades` VALUES ('15', '1', 'Proyecto Sociotecnologico ', 'Informatica', 'MA', '--', '--', '10:30', '12:00', '--', '--', '--', '--', '--', '--');
INSERT INTO `unidades` VALUES ('17', '1', 'Prueba final', 'Agroalimentaria', 'MA-J', '--', '--', '11:27', '11:32', '--', '--', '04:28', '11:33', '--', '--');
