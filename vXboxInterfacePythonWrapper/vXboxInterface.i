%module vXboxInterface

int		 isVBusExists(void);
int		 GetNumEmptyBusSlots(unsigned char * nSlots);
int	 	 isControllerExists(unsigned int UserIndex);
int	 	 isControllerOwned(unsigned int UserIndex);


// Virtual device Plug-In/Unplug
int	 	 PlugIn(unsigned int UserIndex);
int	 	 UnPlug(unsigned int UserIndex);
int	 	 UnPlugForce(unsigned int UserIndex);

// Data Transfer (Data to the device)
int	 	 SetBtnA(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnB(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnX(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnY(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnStart(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnBack(unsigned int UserIndex, unsigned int Press);
int	 	 SetBtnLT(unsigned int UserIndex, unsigned int Press); // Left Thumb/Stick
int	 	 SetBtnRT(unsigned int UserIndex, unsigned int Press); // Right Thumb/Stick
int	 	 SetBtnLB(unsigned int UserIndex, unsigned int Press); // Left Bumper
int	 	 SetBtnRB(unsigned int UserIndex, unsigned int Press); // Right Bumper
int	 	 SetBtnGD(unsigned int UserIndex, unsigned int Press); // Guide Button (Undocumanted)
int	 	 SetTriggerL(unsigned int UserIndex, unsigned char Value); // Left Trigger
int	 	 SetTriggerR(unsigned int UserIndex, unsigned char Value); // Right Trigger
int	 	 SetAxisX(unsigned int UserIndex, int Value); // Left Stick X
int	 	 SetAxisY(unsigned int UserIndex, int Value); // Left Stick Y
int	 	 SetAxisRx(unsigned int UserIndex, int Value); // Right Stick X
int	 	 SetAxisRy(unsigned int UserIndex, int Value); // Right Stick Y
int	 	 SetDpadUp(unsigned int UserIndex);
int	 	 SetDpadRight(unsigned int UserIndex);
int	 	 SetDpadDown(unsigned int UserIndex);
int	 	 SetDpadLeft(unsigned int UserIndex);
int	 	 SetDpadOff(unsigned int UserIndex);
int  	 SetDpad(unsigned int UserIndex, int Value);
