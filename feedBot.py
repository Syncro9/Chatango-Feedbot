import ch
import sys
import time
import feedparser

class TestBot(ch.RoomManager):

     def onInit(self):
         self.setNameColor("F9F")
         self.setFontColor("F33")
         self.setFontFace("1")
         self.setFontSize(10)
         self.enableBg()
         self.enableRecording()

     def check(self, room):
         try:
            feed = feedparser.parse('http://anime2enjoy.com/feed/atom')
            xml = feed.entries[0]
            lastupdated = xml['updated']
            time.sleep(1)
            feed = feedparser.parse('http://anime2enjoy.com/feed/atom')
            xml = feed.entries[0]
            updated = xml['updated']
            author = xml['author']
            title = xml['title']
            link = xml['id']
            if not (lastupdated == updated):
                print("New update on A2E")
                mesg = ' published a new post named: '
                room.message(author + mesg + '"' + title + '"' + ' Link: ' + link)
            else:
                print("No new feed update on A2E")
         except:
             print("Error")
			
     def onConnect(self, room):
         self.setInterval(3, self.check, room)
         print("Connected!")

rooms = ["anime2enjoy-a2e"]
def hexc(e):
    et, ev, tb = sys.exc_info()
    if not tb:
        print(str(e))
    while tb:
        lineno = tb.tb_lineno
        fn = tb.tb_frame.f_code.co_filename
        tb = tb.tb_next
        print("(%s:%i) %s" % (fn, lineno, str(e)))

if __name__ == "__main__":
    error = 0
    try:
        TestBot.easy_start(rooms, "", "")
    except KeyboardInterrupt:
        print("[ERR] Console initiated a kill.")
    except Exception as e:
        print("[ERR] Fatal error.")
        error = 1
        hexc(e)

    if error == 1:
        print("Screenshot the error and send it to Syncro then restart me.")
        time.sleep(1000)
        print("[INF] Shutting down..")
