#include <iostream>
#include <string>
#include "familyclass.h"
using namespace std;


/*
FUNCTION IMPLEMENTED IN THIS ASSIGNMENT ARE - 

1. TAKING A DOUBLY LINKED LIST AS INPUT
2. REMOVING ANY MEMBER OF THE FAMILY FROM THE LIST, USERS CHOICE ALSO GIVEN
3.PRINTING A DOUBLY LINKED LIST
4.FAMILY CLASS(MADE FOR IMPLEMENTING DOUBLY LINKED LIST)
*/


// USING THIS FUNCTION USER CAN SPECIFY THE SIZE OF HIS FAMILY AND THEN INPUT NAME AND AGE OF EVERY MEMBER
Family *takeinputand_appendatlast()
{

    int n;
    cout << "ENTER THE SIZE OF THE FAMILY : ";
    cin >> n;
    cout << endl;

    Family *head = NULL;
    Family *nxt = NULL;
    Family *previous = NULL;

    for (int i = 1; i <= n; i++)
    {
        string s;
        cout << "enter " << i << "th family member name : ";
        cin >> s;

        int age;
        cout << "Enter " << i << "th Family memeber age : ";
        cin >> age;

        Family *newmem = new Family(s, age);

        if (head == NULL)
        {
            head = newmem;
            nxt = newmem;
            previous = newmem;
        }
        else
        {
            previous->next = newmem;
            newmem->prev = previous;
            nxt = newmem;
            previous = nxt;
        }
    }
    return head;
}

//REMOVE ANY MEMBER OF THE FAMILY .
Family *remove_element_from_index_i(Family *head, int i)
{
    if (head == NULL)
    {
        return head;
    }
    Family *temp = head;
    if (i == 0)
    {
        temp = temp->next;
        temp->prev = NULL;
        head = temp;
        return head;
    }
    else
    {
        int count = 0;
        Family *temp1 = head;
        Family *temp2 = NULL;

        while (count < (i - 1))
        {
            temp1 = temp1->next;
            count++;
        }
        Family *to_be_deleted = temp1->next;
        temp2 = to_be_deleted->next;
        temp1->next = temp2;
        temp2->prev = temp1;

        delete to_be_deleted;
        return head;
    }
}

// THIS FUNCTION WITH PRINT EVERY MEMEBER OF THE LIST
void printdoubleLL(Family *head)
{
    Family *temp = head;
    cout << endl
         << "FAMILY TREE--" << endl;
    while (temp != NULL)
    {
        cout << "Members name : " << temp->name << " "
             << "Memebers age : " << temp->age << endl;
        temp = temp->next;
    }
}

int main()
{

    // taking input and appending it at the end of the linked list;
    Family *head = takeinputand_appendatlast();
    printdoubleLL(head);

    // remove a family memeber from anywhere in the list
    int i;
    cin >> i;
    Family *remo = remove_element_from_index_i(head, i);
    printdoubleLL(remo);
}
