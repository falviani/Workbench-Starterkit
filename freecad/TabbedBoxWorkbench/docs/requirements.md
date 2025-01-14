# This specifies the data structures, extensibility structure, and implementation requirements for this workbench

## **Required Data**

There are 3 types of data required. (1) Geometry data - the Freecad objects created/modified by this workbench.
(2) Path workbench data - the data for the Path job created, and its commands, etc. Hopefully
this is  complete enough to be exported as gCode and used directly to create the specified box.
(3) Internal data. There is a considerable amount of data needed to be able
to manipulate the above 2 data classes. Some of it will be global, to be usable
by any box variant, while other is working data for the common implementation
algorithms.

**Terminology**
For consistency I am using the following specific terminology (not sure this is completely standard):

* Tab - the stock that projects out to the outside dimension of the box

* Gap - the space between tabs. This must be the same width as the tab for them to interlace

* Slot - hole in a plate that a tab can be inserted into; the 2 plates involved are at right angles

* Divider - a plate inside a box, with tabs through slots in 2 opposite plates. Can cross other dividers.

* Divider slot - allows dividers to cross.

## **Extensibility**

Extensibility is implemented by having a base class ("basevariant")
 which provides the public interface, and 1 derived class for each type of box which can be generated. It is probable that common utility methods
 will be implemented in the basevariant class.

Custom "support" classes will be created in a separate support module to be imported. This should simplify code management.

 A box generator will consist of the derived class for the code, 1 or more classes for the required dialog(s) that is generated by converting a *.ui file created by the QTdesigner app (in the same folder as the command using it)
 and the icons, etc. that it needs to function. Thus, the 'fancybox' generator will consist of
 
* fancybox.py (actual code),

* fancyDialog.py (derived from resources/ui-files)

* resources/svg and png files (for use in the dialogs and tabs).

## **Additional plate types (more extensibility)**

Future box types can require plates beyond the outside ones in the basic variant. These can include various dividers, etc. These may require additional geometry that modify basic 'outside' plates, such as holes for divider tabs to be fitted into.

Should consider using multiple inheritance here, where there's 1 or more "basic variants" for the additional plates that are added into the specific variants that require them. **Look up details of how this is done in Python.** All concrete derived classes will still inherit at least from the basic variant. **An alternative:** have the 'extra plates' class inherit from the basic variant; concrete variants can inherit from either as appropriate.

## **Proposed box types**

A crude initial inheritance tree:

![](reqImg_01.png)

## **Construction Process Notes**
1) The plates making up a box must be constructed in a specific order in order to ensure the tabs are aligned properly.

2) A plate starts with a list of vertices. They are then converted into line segments, which are converted into a wire. This is finally converted into a shape. **Only shapes can be added to a FreeCAD document.**

3) The list of vertices is constructed with an origin at (0,0,0) and transformed afterwards to place it within the enclosing stock. A quick search suggests the **Draft** workbench is used to rotate and move shapes.

4) A simple method to fit a plate into a stock is needed, trying several orientations to do so. If an orientation fits that will be applied to the plate before it is added to the stock.

5) It is probably necessary to define a function that will (crudely) test the bounding rect of the next plate to be constructed to see if it can be fitted into the currently active stock; if not a new stock is constructed and made active for the next plate to be added to. Probably can take advantage of the 'fitting' method suggested above.