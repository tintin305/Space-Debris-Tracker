Create the model.
Then, in the construct tab select the line, then choose where the line should go from and to.
Add a workplane once the lines have been added.
Select the frequency range and how many frequencies should be looked at (this is in the Source/Load tab >> Frequency button)
Source/Load tab create a wire port (select where on the wire you want this), then on the port on the left bar right click on the port and select: Voltage Source
On the request tab, request the results that you want out of the system, this can include the far fields, near fields, etc. 
Then create a mesh and specify the wire segment radius
On the Solve/Run tab, select FEKO solver, and once this has run, select POSTFEKO