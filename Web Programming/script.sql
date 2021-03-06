USE [master]
GO
/****** Object:  Database [Trims]    Script Date: 4/25/2019 10:21:20 AM ******/
CREATE DATABASE [Trims]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Trims', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Trims.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Trims_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Trims_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [Trims] SET COMPATIBILITY_LEVEL = 130
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Trims].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Trims] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Trims] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Trims] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Trims] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Trims] SET ARITHABORT OFF 
GO
ALTER DATABASE [Trims] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Trims] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Trims] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Trims] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Trims] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Trims] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Trims] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Trims] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Trims] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Trims] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Trims] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Trims] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Trims] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Trims] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Trims] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Trims] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Trims] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Trims] SET RECOVERY FULL 
GO
ALTER DATABASE [Trims] SET  MULTI_USER 
GO
ALTER DATABASE [Trims] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Trims] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Trims] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Trims] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Trims] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'Trims', N'ON'
GO
ALTER DATABASE [Trims] SET QUERY_STORE = OFF
GO
USE [Trims]
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO
USE [Trims]
GO
/****** Object:  Schema [Py]    Script Date: 4/25/2019 10:21:20 AM ******/
CREATE SCHEMA [Py]
GO
USE [Trims]
GO
/****** Object:  Sequence [Py].[ToolImageCounter]    Script Date: 4/25/2019 10:21:20 AM ******/
CREATE SEQUENCE [Py].[ToolImageCounter] 
 AS [bigint]
 START WITH 1
 INCREMENT BY 1
 MINVALUE -9223372036854775808
 MAXVALUE 9223372036854775807
 CACHE 
GO
/****** Object:  Table [Py].[ApprovedUser]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[ApprovedUser](
	[userid] [int] NOT NULL,
	[effectivedt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Audit_Out]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Audit_Out](
	[aoid] [int] NOT NULL,
	[toolid] [int] NOT NULL,
	[quantity] [int] NOT NULL,
	[effectivedt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[BookedToolIssue]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[BookedToolIssue](
	[btiid] [int] NOT NULL,
	[tiid] [int] NOT NULL,
	[bookeddt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[BookedToolIssueOverRule]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[BookedToolIssueOverRule](
	[btiid] [int] NOT NULL,
	[quantity] [int] NOT NULL,
	[fromdt] [datetime] NOT NULL,
	[tilldt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[DisapprovedUser]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[DisapprovedUser](
	[userid] [int] NOT NULL,
	[effectivedt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Issue]    Script Date: 4/25/2019 10:21:20 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Issue](
	[issueid] [int] IDENTITY(1,1) NOT NULL,
	[projectid] [int] NOT NULL,
	[userid] [int] NOT NULL,
	[raiseddt] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[issueid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[IssuedToolIssue]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[IssuedToolIssue](
	[itiid] [int] NOT NULL,
	[tiid] [int] NOT NULL,
	[issueddt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Project]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Project](
	[projectid] [int] IDENTITY(1,1) NOT NULL,
	[projectname] [varchar](50) NOT NULL,
	[title] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[projectid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[PurchaseOrder]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[PurchaseOrder](
	[poid] [int] IDENTITY(1,1) NOT NULL,
	[vendor] [varchar](50) NOT NULL,
	[ordereddt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[RequestedToolIssue]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[RequestedToolIssue](
	[reqtiid] [int] IDENTITY(1,1) NOT NULL,
	[tiid] [int] NOT NULL,
	[quantity] [int] NOT NULL,
	[fromdt] [datetime] NOT NULL,
	[tilldt] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[reqtiid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[ReturnToolIssue]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[ReturnToolIssue](
	[rettiid] [int] NOT NULL,
	[tiid] [int] NOT NULL,
	[returneddt] [datetime] NOT NULL,
	[quantity] [int] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Tool]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Tool](
	[toolid] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](50) NOT NULL,
	[picturepath] [varchar](50) NULL,
	[quantity] [int] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Tool_PurchaseOrder]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Tool_PurchaseOrder](
	[toolid] [int] NOT NULL,
	[poid] [int] NOT NULL,
	[quantity] [int] NOT NULL,
	[expectedarrivaldt] [datetime] NOT NULL,
	[userid] [int] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[ToolIssue]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[ToolIssue](
	[tiid] [int] IDENTITY(1,1) NOT NULL,
	[issueid] [int] NOT NULL,
	[toolid] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[tiid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[UserCredential]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[UserCredential](
	[userid] [int] NOT NULL,
	[password] [varchar](50) NOT NULL,
	[effectivedt] [datetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [Py].[Usr]    Script Date: 4/25/2019 10:21:21 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Py].[Usr](
	[userid] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](50) NOT NULL,
	[email] [varchar](50) NOT NULL
) ON [PRIMARY]

GO
ALTER TABLE [Py].[ApprovedUser] ADD  DEFAULT (getdate()) FOR [effectivedt]
GO
ALTER TABLE [Py].[Audit_Out] ADD  DEFAULT (getdate()) FOR [effectivedt]
GO
ALTER TABLE [Py].[DisapprovedUser] ADD  DEFAULT (getdate()) FOR [effectivedt]
GO
ALTER TABLE [Py].[Issue] ADD  CONSTRAINT [DF_YourTable]  DEFAULT (getdate()) FOR [raiseddt]
GO
ALTER TABLE [Py].[PurchaseOrder] ADD  DEFAULT (getdate()) FOR [ordereddt]
GO
ALTER TABLE [Py].[UserCredential] ADD  DEFAULT (getdate()) FOR [effectivedt]
GO
USE [master]
GO
ALTER DATABASE [Trims] SET  READ_WRITE 
GO
