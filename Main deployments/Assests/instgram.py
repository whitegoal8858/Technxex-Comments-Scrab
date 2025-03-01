import instaloader
import argparse

def main():
    # Set up command-line arguments with a default target profile
    parser = argparse.ArgumentParser(
        description="Download Instagram posts and print captions and comments using Instaloader."
    )
    # Make target_profile optional with default "exampleuser"
    parser.add_argument("target_profile", nargs="?", default="exampleuser", 
                        help="Instagram username to download posts from (default: exampleuser)")
    parser.add_argument("--login", help="Your Instagram username (if login is required)", default=None)
    parser.add_argument("--password", help="Your Instagram password (if login is required)", default=None)
    args = parser.parse_args()

    # Create an Instaloader instance
    L = instaloader.Instaloader()

    # Log in if credentials are provided
    if args.login and args.password:
        try:
            L.login(args.login, args.password)
            print(f"Logged in as {args.login}")
        except Exception as e:
            print("Error during login:", e)
            return

    try:
        # Load the target profile
        profile = instaloader.Profile.from_username(L.context, args.target_profile)
    except Exception as e:
        print("Error loading profile:", e)
        return

    # Iterate over posts in the profile
    for post in profile.get_posts():
        print("=" * 50)
        print("Post URL: https://www.instagram.com/p/" + post.shortcode)
        print("Caption:", post.caption)
        print("Date:", post.date)
        print("Number of Comments:", post.comments)
        print("Comments:")
        # Iterate over comments in the post
        for comment in post.get_comments():
            print(f" - {comment.owner.username}: {comment.text}")
        print("=" * 50, "\n")

if __name__ == "_main_":
    main()