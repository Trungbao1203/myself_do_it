class Video:
	def __init__ (self, title, link):
		self.title = title
		self.link = link

def read_videos():
	videos = []
	total = input("Enter number do you have want: ")
	for i in range ( int(total)):
		print("Video number: ", i+1)
		title = input("Enter title: ")
		link = input("Enter link: ")
		vid = Video(title, link)
		videos.append(vid)
	return videos

def write_video_txt(videos):
	total = len(videos)
	with open ("data_44.txt", "w") as file:
		file.write( str(total) + "\n") # Hiện ra số lượng video ở đầu file data
		for i in range (total):
			file.write(videos[i].title + "\n")
			file.write(videos[i].link + "\n")

def read_video_txt():
	data = []
	with open ("data_44.txt", "r") as file:
		total_video = file.readline() # đọc số lượng video ở đầu file data là có bao nhiêu?
		for i in range ( int(total_video) ):
			title = file.readline()
			link = file.readline()
			video = Video(title, link)
			data.append(video)
	return data

def print_videos(data):
	print("---- Display ---- ")
	for i in range (len(data)):
		print("Video title: ", data[i].title, end="")
		print("Video link: ", data[i].link, end="")

def main():
	videos = read_videos()
	write_video_txt(videos)
	data = read_video_txt()
	print_videos(data)
main()
















































# class Video:
# 	def __init__ (self, title, link):
# 		self.title = title
# 		self.link = link

# def read_video():
# 	title = input("Enter the title: ")
# 	link = input("Enter the link: ")
# 	video = Video (title,link)
# 	return video

# def print_video(video):
# 	print("-----")
# 	print("Title have: ", video.title)
# 	print("Link have: ", video.link)

# def read_videos():
# 	videos = []
# 	total_videos = int(input("Enter how many videos: "))
# 	for i in range (total_videos):
# 		print("-----Enter video ", i+1)
# 		vid = read_video()
# 		videos.append(vid)
# 	return videos
# def print_videos(videos):
# 	for i in range (len(videos)):
# 		print_video(videos[i])
# def write_txt():
# 	with open ("data.txt", "w") as file:
# 		for i in range (len(videos)):
# 			file.write()

# def main():
# 	videos = read_videos()
# 	print_videos(videos)
	
	
# main()