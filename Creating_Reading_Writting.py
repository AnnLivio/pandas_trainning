{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8b0f1eaa",
   "metadata": {
    "papermill": {
     "duration": 0.005872,
     "end_time": "2024-06-08T07:50:34.538179",
     "exception": false,
     "start_time": "2024-06-08T07:50:34.532307",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**This notebook is an exercise in the [Pandas](https://www.kaggle.com/learn/pandas) course.  You can reference the tutorial at [this link](https://www.kaggle.com/residentmario/creating-reading-and-writing).**\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ecf5000",
   "metadata": {
    "papermill": {
     "duration": 0.004904,
     "end_time": "2024-06-08T07:50:34.548516",
     "exception": false,
     "start_time": "2024-06-08T07:50:34.543612",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Introduction\n",
    "\n",
    "The first step in most data analytics projects is reading the data file. In this exercise, you'll create Series and DataFrame objects, both by hand and by reading data files.\n",
    "\n",
    "Run the code cell below to load libraries you will need (including code to check your answers)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7a37c327",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:34.561076Z",
     "iopub.status.busy": "2024-06-08T07:50:34.560572Z",
     "iopub.status.idle": "2024-06-08T07:50:37.197409Z",
     "shell.execute_reply": "2024-06-08T07:50:37.196159Z"
    },
    "papermill": {
     "duration": 2.646305,
     "end_time": "2024-06-08T07:50:37.200083",
     "exception": false,
     "start_time": "2024-06-08T07:50:34.553778",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup complete.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "pd.set_option('display.max_rows', 5)\n",
    "from learntools.core import binder; binder.bind(globals())\n",
    "from learntools.pandas.creating_reading_and_writing import *\n",
    "print(\"Setup complete.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f274bb9",
   "metadata": {
    "papermill": {
     "duration": 0.005378,
     "end_time": "2024-06-08T07:50:37.210957",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.205579",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35c86f50",
   "metadata": {
    "papermill": {
     "duration": 0.005028,
     "end_time": "2024-06-08T07:50:37.221776",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.216748",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 1.\n",
    "\n",
    "In the cell below, create a DataFrame `fruits` that looks like this:\n",
    "\n",
    "![](https://storage.googleapis.com/kaggle-media/learn/images/Ax3pp2A.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6675190b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.234602Z",
     "iopub.status.busy": "2024-06-08T07:50:37.234227Z",
     "iopub.status.idle": "2024-06-08T07:50:37.253716Z",
     "shell.execute_reply": "2024-06-08T07:50:37.252728Z"
    },
    "papermill": {
     "duration": 0.028981,
     "end_time": "2024-06-08T07:50:37.256228",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.227247",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.16666666666666666, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"1_FruitDfCreation\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Apples</th>\n",
       "      <th>Bananas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Apples  Bananas\n",
       "0      30       21"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.\n",
    "fruits = pd.DataFrame({'Apples':[30], 'Bananas':[21]})\n",
    "\n",
    "# Check your answer\n",
    "q1.check()\n",
    "fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c95cb5e8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.269785Z",
     "iopub.status.busy": "2024-06-08T07:50:37.269380Z",
     "iopub.status.idle": "2024-06-08T07:50:37.274737Z",
     "shell.execute_reply": "2024-06-08T07:50:37.273441Z"
    },
    "papermill": {
     "duration": 0.015281,
     "end_time": "2024-06-08T07:50:37.277462",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.262181",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q1.hint()\n",
    "#q1.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e58f770",
   "metadata": {
    "papermill": {
     "duration": 0.005556,
     "end_time": "2024-06-08T07:50:37.289051",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.283495",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 2.\n",
    "\n",
    "Create a dataframe `fruit_sales` that matches the diagram below:\n",
    "\n",
    "![](https://storage.googleapis.com/kaggle-media/learn/images/CHPn7ZF.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a64188d5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.304281Z",
     "iopub.status.busy": "2024-06-08T07:50:37.303851Z",
     "iopub.status.idle": "2024-06-08T07:50:37.322417Z",
     "shell.execute_reply": "2024-06-08T07:50:37.321180Z"
    },
    "papermill": {
     "duration": 0.02975,
     "end_time": "2024-06-08T07:50:37.325132",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.295382",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.16666666666666666, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"2_FruitSalesDfCreation\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Apples</th>\n",
       "      <th>Bananas</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017 Sales</th>\n",
       "      <td>35</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018 Sales</th>\n",
       "      <td>41</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Apples  Bananas\n",
       "2017 Sales      35       21\n",
       "2018 Sales      41       34"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.\n",
    "fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21,34]}, index=['2017 Sales', '2018 Sales'])\n",
    "\n",
    "# Check your answer\n",
    "q2.check()\n",
    "fruit_sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4019e285",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.340211Z",
     "iopub.status.busy": "2024-06-08T07:50:37.339726Z",
     "iopub.status.idle": "2024-06-08T07:50:37.344507Z",
     "shell.execute_reply": "2024-06-08T07:50:37.343410Z"
    },
    "papermill": {
     "duration": 0.015606,
     "end_time": "2024-06-08T07:50:37.347105",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.331499",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q2.hint()\n",
    "#q2.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d9187a0",
   "metadata": {
    "papermill": {
     "duration": 0.006154,
     "end_time": "2024-06-08T07:50:37.359549",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.353395",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 3.\n",
    "\n",
    "Create a variable `ingredients` with a Series that looks like:\n",
    "\n",
    "```\n",
    "Flour     4 cups\n",
    "Milk       1 cup\n",
    "Eggs     2 large\n",
    "Spam       1 can\n",
    "Name: Dinner, dtype: object\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a0ca6b51",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.375356Z",
     "iopub.status.busy": "2024-06-08T07:50:37.373964Z",
     "iopub.status.idle": "2024-06-08T07:50:37.388187Z",
     "shell.execute_reply": "2024-06-08T07:50:37.387136Z"
    },
    "papermill": {
     "duration": 0.024416,
     "end_time": "2024-06-08T07:50:37.390595",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.366179",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.16666666666666666, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"3_RecipeSeriesCreation\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Flour     4 cups\n",
       "Milk       1 cup\n",
       "Eggs     2 large\n",
       "Spam       1 can\n",
       "Name: Dinner, dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour','Milk','Eggs','Spam'], name='Dinner')\n",
    "\n",
    "# Check your answer\n",
    "q3.check()\n",
    "ingredients"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ce330c57",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.406207Z",
     "iopub.status.busy": "2024-06-08T07:50:37.405805Z",
     "iopub.status.idle": "2024-06-08T07:50:37.410409Z",
     "shell.execute_reply": "2024-06-08T07:50:37.409226Z"
    },
    "papermill": {
     "duration": 0.015587,
     "end_time": "2024-06-08T07:50:37.412897",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.397310",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q3.hint()\n",
    "#q3.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f0b1a95",
   "metadata": {
    "papermill": {
     "duration": 0.006601,
     "end_time": "2024-06-08T07:50:37.426421",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.419820",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 4.\n",
    "\n",
    "Read the following csv dataset of wine reviews into a DataFrame called `reviews`:\n",
    "\n",
    "![](https://storage.googleapis.com/kaggle-media/learn/images/74RCZtU.png)\n",
    "\n",
    "The filepath to the csv file is `../input/wine-reviews/winemag-data_first150k.csv`. The first few lines look like:\n",
    "\n",
    "```\n",
    ",country,description,designation,points,price,province,region_1,region_2,variety,winery\n",
    "0,US,\"This tremendous 100% varietal wine[...]\",Martha's Vineyard,96,235.0,California,Napa Valley,Napa,Cabernet Sauvignon,Heitz\n",
    "1,Spain,\"Ripe aromas of fig, blackberry and[...]\",Carodorum Selección Especial Reserva,96,110.0,Northern Spain,Toro,,Tinta de Toro,Bodega Carmen Rodríguez\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "df00bbb8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:37.441524Z",
     "iopub.status.busy": "2024-06-08T07:50:37.441123Z",
     "iopub.status.idle": "2024-06-08T07:50:38.469415Z",
     "shell.execute_reply": "2024-06-08T07:50:38.468310Z"
    },
    "papermill": {
     "duration": 1.038786,
     "end_time": "2024-06-08T07:50:38.471856",
     "exception": false,
     "start_time": "2024-06-08T07:50:37.433070",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.16666666666666666, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"4_ReadWineCsv\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>description</th>\n",
       "      <th>designation</th>\n",
       "      <th>points</th>\n",
       "      <th>price</th>\n",
       "      <th>province</th>\n",
       "      <th>region_1</th>\n",
       "      <th>region_2</th>\n",
       "      <th>variety</th>\n",
       "      <th>winery</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>US</td>\n",
       "      <td>This tremendous 100% varietal wine hails from ...</td>\n",
       "      <td>Martha's Vineyard</td>\n",
       "      <td>96</td>\n",
       "      <td>235.0</td>\n",
       "      <td>California</td>\n",
       "      <td>Napa Valley</td>\n",
       "      <td>Napa</td>\n",
       "      <td>Cabernet Sauvignon</td>\n",
       "      <td>Heitz</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spain</td>\n",
       "      <td>Ripe aromas of fig, blackberry and cassis are ...</td>\n",
       "      <td>Carodorum Selección Especial Reserva</td>\n",
       "      <td>96</td>\n",
       "      <td>110.0</td>\n",
       "      <td>Northern Spain</td>\n",
       "      <td>Toro</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tinta de Toro</td>\n",
       "      <td>Bodega Carmen Rodríguez</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>150928</th>\n",
       "      <td>France</td>\n",
       "      <td>A perfect salmon shade, with scents of peaches...</td>\n",
       "      <td>Grand Brut Rosé</td>\n",
       "      <td>90</td>\n",
       "      <td>52.0</td>\n",
       "      <td>Champagne</td>\n",
       "      <td>Champagne</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Champagne Blend</td>\n",
       "      <td>Gosset</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>150929</th>\n",
       "      <td>Italy</td>\n",
       "      <td>More Pinot Grigios should taste like this. A r...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>90</td>\n",
       "      <td>15.0</td>\n",
       "      <td>Northeastern Italy</td>\n",
       "      <td>Alto Adige</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Pinot Grigio</td>\n",
       "      <td>Alois Lageder</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>150930 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       country                                        description  \\\n",
       "0           US  This tremendous 100% varietal wine hails from ...   \n",
       "1        Spain  Ripe aromas of fig, blackberry and cassis are ...   \n",
       "...        ...                                                ...   \n",
       "150928  France  A perfect salmon shade, with scents of peaches...   \n",
       "150929   Italy  More Pinot Grigios should taste like this. A r...   \n",
       "\n",
       "                                 designation  points  price  \\\n",
       "0                          Martha's Vineyard      96  235.0   \n",
       "1       Carodorum Selección Especial Reserva      96  110.0   \n",
       "...                                      ...     ...    ...   \n",
       "150928                       Grand Brut Rosé      90   52.0   \n",
       "150929                                   NaN      90   15.0   \n",
       "\n",
       "                  province     region_1 region_2             variety  \\\n",
       "0               California  Napa Valley     Napa  Cabernet Sauvignon   \n",
       "1           Northern Spain         Toro      NaN       Tinta de Toro   \n",
       "...                    ...          ...      ...                 ...   \n",
       "150928           Champagne    Champagne      NaN     Champagne Blend   \n",
       "150929  Northeastern Italy   Alto Adige      NaN        Pinot Grigio   \n",
       "\n",
       "                         winery  \n",
       "0                         Heitz  \n",
       "1       Bodega Carmen Rodríguez  \n",
       "...                         ...  \n",
       "150928                   Gosset  \n",
       "150929            Alois Lageder  \n",
       "\n",
       "[150930 rows x 10 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)\n",
    "\n",
    "# Check your answer\n",
    "q4.check()\n",
    "reviews"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a7c1f85a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:38.488334Z",
     "iopub.status.busy": "2024-06-08T07:50:38.487913Z",
     "iopub.status.idle": "2024-06-08T07:50:38.496411Z",
     "shell.execute_reply": "2024-06-08T07:50:38.495192Z"
    },
    "papermill": {
     "duration": 0.019807,
     "end_time": "2024-06-08T07:50:38.498880",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.479073",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 1, \"questionId\": \"4_ReadWineCsv\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> Note that the csv file begins with an unnamed column of increasing integers. We want this to be used as the index. Check out the description of the `index_col` keyword argument in [the docs for `read_csv`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)."
      ],
      "text/plain": [
       "Hint: Note that the csv file begins with an unnamed column of increasing integers. We want this to be used as the index. Check out the description of the `index_col` keyword argument in [the docs for `read_csv`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)."
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q4.hint()\n",
    "#q4.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6de526bd",
   "metadata": {
    "papermill": {
     "duration": 0.007091,
     "end_time": "2024-06-08T07:50:38.513425",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.506334",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 5.\n",
    "\n",
    "Run the cell below to create and display a DataFrame called `animals`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4e257725",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:38.531113Z",
     "iopub.status.busy": "2024-06-08T07:50:38.529972Z",
     "iopub.status.idle": "2024-06-08T07:50:38.540685Z",
     "shell.execute_reply": "2024-06-08T07:50:38.539564Z"
    },
    "papermill": {
     "duration": 0.022394,
     "end_time": "2024-06-08T07:50:38.543457",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.521063",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cows</th>\n",
       "      <th>Goats</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Year 1</th>\n",
       "      <td>12</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Year 2</th>\n",
       "      <td>20</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Cows  Goats\n",
       "Year 1    12     22\n",
       "Year 2    20     19"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])\n",
    "animals"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49bd031a",
   "metadata": {
    "papermill": {
     "duration": 0.007265,
     "end_time": "2024-06-08T07:50:38.558182",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.550917",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "In the cell below, write code to save this DataFrame to disk as a csv file with the name `cows_and_goats.csv`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "38a8bc1d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:38.575062Z",
     "iopub.status.busy": "2024-06-08T07:50:38.574669Z",
     "iopub.status.idle": "2024-06-08T07:50:38.591756Z",
     "shell.execute_reply": "2024-06-08T07:50:38.590620Z"
    },
    "papermill": {
     "duration": 0.028706,
     "end_time": "2024-06-08T07:50:38.594415",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.565709",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.16666666666666666, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"5_SaveAnimalsCsv\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Your code goes here\n",
    "animals.to_csv(\"cows_and_goats.csv\")\n",
    "# Check your answer\n",
    "q5.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "55c7eae5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-06-08T07:50:38.612347Z",
     "iopub.status.busy": "2024-06-08T07:50:38.611931Z",
     "iopub.status.idle": "2024-06-08T07:50:38.616630Z",
     "shell.execute_reply": "2024-06-08T07:50:38.615461Z"
    },
    "papermill": {
     "duration": 0.016322,
     "end_time": "2024-06-08T07:50:38.618831",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.602509",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q5.hint()\n",
    "#q5.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dda456f7",
   "metadata": {
    "papermill": {
     "duration": 0.007607,
     "end_time": "2024-06-08T07:50:38.634410",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.626803",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Keep going\n",
    "\n",
    "Move on to learn about **[indexing, selecting and assigning](https://www.kaggle.com/residentmario/indexing-selecting-assigning)**."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0225850",
   "metadata": {
    "papermill": {
     "duration": 0.007549,
     "end_time": "2024-06-08T07:50:38.649834",
     "exception": false,
     "start_time": "2024-06-08T07:50:38.642285",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "---\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/pandas/discussion) to chat with other learners.*"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 655,
     "sourceId": 1252,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 2321,
     "sourceId": 3919,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 2894,
     "sourceId": 4877,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 3491,
     "sourceId": 5624,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 1442,
     "sourceId": 8172,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 9366,
     "sourceId": 13206,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 179555,
     "sourceId": 403916,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 4549,
     "sourceId": 466349,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 2478,
     "sourceId": 1151655,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 10128,
     "sourceId": 5438389,
     "sourceType": "datasetVersion"
    }
   ],
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 7.538059,
   "end_time": "2024-06-08T07:50:39.179524",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-06-08T07:50:31.641465",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
