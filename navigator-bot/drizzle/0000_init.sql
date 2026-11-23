CREATE TABLE "guard_counts" (
	"key" text PRIMARY KEY NOT NULL,
	"n" integer NOT NULL,
	"expires_at" timestamp with time zone NOT NULL
);
--> statement-breakpoint
CREATE TABLE "guard_spend" (
	"channel" text NOT NULL,
	"day" integer NOT NULL,
	"usd" double precision DEFAULT 0 NOT NULL,
	CONSTRAINT "guard_spend_channel_day_pk" PRIMARY KEY("channel","day")
);
--> statement-breakpoint
CREATE TABLE "inbox" (
	"id" text PRIMARY KEY NOT NULL,
	"channel" text NOT NULL,
	"thread_id" text NOT NULL,
	"user_key" text NOT NULL,
	"text" text NOT NULL,
	"attempts" integer DEFAULT 0 NOT NULL,
	"received_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "kb_state" (
	"id" integer PRIMARY KEY DEFAULT 1 NOT NULL,
	"commit" text,
	"counts" jsonb NOT NULL,
	"updated_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "turns" (
	"id" bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY (sequence name "turns_id_seq" INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START WITH 1 CACHE 1),
	"user_key" text NOT NULL,
	"role" text NOT NULL,
	"text" text NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"user_key" text PRIMARY KEY NOT NULL,
	"country" text,
	"profile" jsonb DEFAULT '{}'::jsonb NOT NULL,
	"summary" text DEFAULT '' NOT NULL,
	"summarised_to" bigint DEFAULT 0 NOT NULL,
	"created_at" timestamp with time zone DEFAULT now() NOT NULL,
	"last_seen" timestamp with time zone DEFAULT now() NOT NULL
);
--> statement-breakpoint
ALTER TABLE "turns" ADD CONSTRAINT "turns_user_key_users_user_key_fk" FOREIGN KEY ("user_key") REFERENCES "public"."users"("user_key") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "turns_user_id" ON "turns" USING btree ("user_key","id");--> statement-breakpoint
CREATE INDEX "turns_created_at" ON "turns" USING btree ("created_at");