# Import modules
import tkinter as tk
import tkinter.messagebox
import manage
import vote

password = "01"

global root
global pswdRoot
global manageRoot
global scoresRoot
global addCandRoot

def fromViewScoresToManagementMenu():
    global scoresRoot
    scoresRoot.destroy()
    goToManagementMenu()

def goToViewScores():
    global manageRoot
    global scoresRoot
    manageRoot.destroy()
    scoresRoot = tk.Tk()
    scoresRoot.title("View scores")
    tk.Label(scoresRoot, text="Scoretable:").grid(row=0, column=0, padx=40, pady=5, columnspan=2)
    scores = manage.viewScores()
    for y,score in enumerate(scores):
        total = y
        for x,col in enumerate(score):
            tk.Label(scoresRoot, text=col).grid(row=y+2, column=x, padx=5, pady=2, sticky=tk.W)
    tk.Button(scoresRoot, text="Back", command=fromViewScoresToManagementMenu).grid(row=total+3, column=0, columnspan=2, pady=5)
    scoresRoot.mainloop()

def addCandSubmit(name):
    global addCandRoot
    manage.addCand(name)
    addCandRoot.destroy()
    goToManagementMenu()

def goToAddCandidate():
    global manageRoot
    global addCandRoot
    manageRoot.destroy()
    addCandRoot = tk.Tk()
    addCandRoot.title("Add candidate")
    tk.Label(addCandRoot, text="Candidate's name:").grid(row=0, column=0, pady=5, padx=5)
    candName = tk.Entry(addCandRoot, width=30)
    candName.grid(row=0, column=1, pady=5, padx=5)
    tk.Button(addCandRoot, text="Submit", command= lambda: addCandSubmit(candName.get())).grid(row=1, column=0, columnspan=2, pady=5, padx=5)
    addCandRoot.mainloop()

def toRemCand(toRem):
    global remCandRoot
    remCandRoot.destroy()
    manage.remCand(toRem)
    goToManagementMenu()

def goToRemCandidate():
    global manageRoot
    global remCandRoot
    manageRoot.destroy()
    remCandRoot = tk.Tk()
    remCandRoot.title("Remove candidate")
    tk.Label(remCandRoot, text="Choose a candidate to remove:").grid(column=0, row=0, pady=5, padx=25)
    candidates = vote.openScores()
    for i,row in enumerate(candidates):
        if(i == 0):
            continue
        tk.Button(remCandRoot, text=str(row[0]), command= lambda i=i: toRemCand(str(i))).grid(row=i, column=0, padx=5, pady=5)
    remCandRoot.mainloop()

def fromManagementMenuToMain():
    global manageRoot
    manageRoot.destroy()
    goToMain()

def goToManagementMenu():
    global manageRoot
    manageRoot = tk.Tk()
    manageRoot.title("Management")
    tk.Label(manageRoot, text="Welcome to the management interface").grid(row=0, column=0, pady=5, padx=15)
    tk.Button(manageRoot, text="View scores", command=goToViewScores).grid(row=1, column=0, pady=5, padx=15)
    tk.Button(manageRoot, text="Add candidate", command=goToAddCandidate).grid(row=2, column=0, pady=5, padx=15)
    tk.Button(manageRoot, text="Remove candidate", command=goToRemCandidate).grid(row=3, column=0, pady=5, padx=15)
    tk.Button(manageRoot, text="Back", command=fromManagementMenuToMain).grid(row=4, column=0, pady=5, padx=15)
    manageRoot.mainloop()


def checkPswd(input):
    global pswdRoot
    if(input != password):
        tk.messagebox.showerror("Incorrect password", "Incorrect password entered. Please try again.")
        pswdRoot.destroy()
        goToManagement()
    else:
        pswdRoot.destroy()
        goToManagementMenu()

def goToManagement():
    global root
    global pswdRoot
    try:
        root.destroy()
    except:
        pass
    pswdRoot = tk.Tk()
    pswdRoot.title("Enter password")

    tk.Label(pswdRoot, text="Password:").grid(row=0, column=0, pady=5, padx=5)
    pswdText = tk.Entry(pswdRoot, show="*", width=30)
    pswdText.grid(row=0, column=1, padx=5)
    tk.Button(pswdRoot, text="Submit", command=lambda: checkPswd(pswdText.get())).grid(row=1, column=1, columnspan=2, pady=5)
    pswdRoot.mainloop()

def goToMain():
    global root
    root = tk.Tk()
    root.title("Voting system")

    tk.Label(root, text="Choose a person to vote for from the list below:").grid(row=0, column=0, padx=15, pady=5)
    candidates = vote.openScores()

    for i,row in enumerate(candidates):
        total = i
        if(i == 0):
            continue
        tk.Button(root, text=str(row[0]), command= lambda i=i: vote.updateVotes(candidates,str(i))).grid(row=i, column=0, padx=5, pady=5)

    tk.Label(root, text="When finished, close this window to finalise vote.").grid(row=total+1, column=0, pady=5)
    tk.Button(root, text="Management", command=goToManagement).grid(row=total+2, column=0, pady=10)

    root.mainloop()

goToMain()