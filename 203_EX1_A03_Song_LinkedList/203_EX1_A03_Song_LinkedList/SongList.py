#!/usr/bin/env python3
"""Linked Lists -> Song List Implementation: Exercise 1

The goal of this exercise is to learn how to create a custom linked list for songs.
Each node in this linked list represent a song.
This data structure consists of a collection of songs(node) which together represent a playlist.
The SongList class contains methods to insert a song, and traversal through the list to print titles.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this tutorial located in same folder.

To test run 'SongList_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""
class SongNode:
    def __init__(self, song_title=None, next = None):
        self.song_title = song_title
        self.next = next

    def add(self, song_title):
        if self.next:
            self.next.add(song_title)
        else:
            self.next = SongNode(song_title)

class SongList:
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        string = ""
        while curr:
            string += str(curr.song_title) + "\n"
            curr = curr.next

        return string[:-1]

    # TODO 1: Traverse through the list and print every song titles
    def printSongs(self):
        print(self)

    # TODO 2: Insert a new song title to the end of the list
    def AddNewSong(self, new_song_title):
        # if not self.head:
        #     self.head = SongNode(new_song_title)
        # elif not self.tail:
        #     self.tail = SongNode(new_song_title)
        #     self.head.next = self.tail
        # else:
        #     self.tail.next = SongNode(new_song_title)
        #     self.tail = self.tail.next

        # Kinda takes away the point of a LinkedList, but since Nodes can be added by accessing the head property,
        #  Nothing could ever be assigned to the Tail which causes unintended behavior.
        self.head.add(new_song_title)