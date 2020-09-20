IF Object_ID('news_articles_cnbc') IS NULL

CREATE TABLE [sigma-coding-test].[dbo].[news_articles_cnbc]
(
    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [type] NVARCHAR(MAX) NULL,
    [article_id] NVARCHAR(MAX) NULL,
    [sponsored] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL
);

