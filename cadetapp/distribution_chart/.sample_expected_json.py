#-----------------------------------------------------------------------------
#
# This file is the sample expected json structure the Distribution Chart
# expected from the controller.
#
#-----------------------------------------------------------------------------


# class ChartTopicData needs JSON like this
data = {
  "topic": [
    {
      "topic_id": "1",
      "sentiment_count": [
        {
          "pos": "15",
          "neu": "5",
          "neg": "14"
        }
      ]
    },
    {
      "topic_id": "2",
      "sentiment_count": [
        {
          "pos": "11",
          "neu": "19",
          "neg": "3"
        }
      ]
    },
    {
      "topic_id": "3",
      "sentiment_count": [
        {
          "pos": "13",
          "neu": "6",
          "neg": "11"
        }
      ]
    },
    {
      "topic_id": "4",
      "sentiment_count": [
        {
          "pos": "19",
          "neu": "2",
          "neg": "8"
        }
      ]
    },
    {
      "topic_id": "5",
      "sentiment_count": [
        {
          "pos": "7",
          "neu": "9",
          "neg": "15"
        }
      ]
    }
  ]
}

# class ChartTopicWordData needs JSON like this
topic_word_data = {
  "topic": [
    {
      "topic_id": "1",
      "words": "happy, good, fun, yay, smile"
    },
    {
      "topic_id": "2",
      "words": "sad, boo, mean, hard, lethal"
    },
    {
      "topic_id": "3",
      "words": "hub, hubba, buh, duh, huh"
    },
    {
      "topic_id": "4",
      "words": "foo, baz, exe, why, zee"
    },
    {
      "topic_id": "5",
      "words": "red, white, blue, yellow, green"
    }
  ]
}
       
# class ChartInstructorData needs JSON like this  
instructor_data = {
  "instructor": [
    {
      "instructor_name": "joe smoe",
      "sentiment_count": [
        {
          "pos": "28",
          "neu": "8",
          "neg": "2"
        }
      ]
    },
    {
      "instructor_name": "nathalie fozz",
      "sentiment_count": [
        {
          "pos": "15",
          "neu": "3",
          "neg": "7"
        }
      ]
    },
    {
      "instructor_name": "beavis butthead",
      "sentiment_count": [
        {
          "pos": "38",
          "neu": "8",
          "neg": "2"
        }
      ]
    },
    {
      "instructor_name": "boaty boatface",
      "sentiment_count": [
        {
          "pos": "19",
          "neu": "2",
          "neg": "8"
        }
      ]
    },
    {
      "instructor_name": "numbly doo",
      "sentiment_count": [
        {
          "pos": "7",
          "neu": "8",
          "neg": "20"
        }
      ]
    }
  ]
}
