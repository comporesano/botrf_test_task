from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "app_user" ALTER COLUMN "first_name" TYPE VARCHAR(50) USING "first_name"::VARCHAR(50);
        ALTER TABLE "app_user" ALTER COLUMN "last_name" TYPE VARCHAR(50) USING "last_name"::VARCHAR(50);
        ALTER TABLE "app_user" ALTER COLUMN "username" TYPE VARCHAR(50) USING "username"::VARCHAR(50);
        CREATE  INDEX "idx_app_user_usernam_7e2b36" ON "app_user" ("username");
        CREATE UNIQUE INDEX "uid_app_user_usernam_7e2b36" ON "app_user" ("username");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_app_user_usernam_7e2b36";
        DROP INDEX "idx_app_user_usernam_7e2b36";
        ALTER TABLE "app_user" ALTER COLUMN "first_name" TYPE TEXT USING "first_name"::TEXT;
        ALTER TABLE "app_user" ALTER COLUMN "last_name" TYPE TEXT USING "last_name"::TEXT;
        ALTER TABLE "app_user" ALTER COLUMN "username" TYPE TEXT USING "username"::TEXT;"""
