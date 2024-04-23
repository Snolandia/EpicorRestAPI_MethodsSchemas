import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReportQtySvc
# Description: Quantity Reporting from MES menu
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckInspResults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckInspResults
   Description: This method validates if InspResults has been entered when the Inspection Data is allowed for the current OprSeq.
   OperationID: CheckInspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLaborEquip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLaborEquip
   Description: This method should call when EquipID is changed
   OperationID: DeleteLaborEquip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborEquip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborEquip
   Description: This method returns the new Labor Equipment
   OperationID: GetNewLaborEquip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReportQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReportQty
   Description: This method returns the new ReportQty dataset in place of the standard GetNew method.
   OperationID: GetNewReportQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReportQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAsmSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAsmSeq
   Description: This method validates the Assembly sequence.
   OperationID: OnChangeAsmSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAsmSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAsmSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: OnChangeEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the Operation sequence.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNextOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNextOprSeq
   Description: This method validates the Next Operation sequence.
   OperationID: OnChangeNextOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNextOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNextOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOprSeq
   Description: This method validates the Operation sequence.
   OperationID: OnChangeOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: This method validates the PCID
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResource
   Description: This method validates the ResourceID.
   OperationID: OnChangeResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReportQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReportQuantity
   Description: This method reports the quantity changes to the database
   OperationID: ReportQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReportQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLaborEquip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLaborEquip
   Description: This method should call when EquipID is changed
   OperationID: UpdateLaborEquip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSerialBeforeSelect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSerialBeforeSelect
   Description: Call before allowing the select of serial numbers
   OperationID: ValidateSerialBeforeSelect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSerialBeforeSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialBeforeSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckInspResults_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Current Job  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  Current AssembleSeq  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  Current OprSeq  """  
      pass

class CheckInspResults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inspectionOK:bool = obj["inspectionOK"]
      pass

      """  output parameters  """  

class DeleteLaborEquip_input:
   """ Required : 
   empID
   equipID
   hedSeq
   dtlSeq
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Current Employee ID  """  
      self.equipID:str = obj["equipID"]
      """  Current Labor Equipment ID  """  
      self.hedSeq:int = obj["hedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.dtlSeq:int = obj["dtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class DeleteLaborEquip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ReportQtyEquipRow:
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      self.EquipID:str = obj["EquipID"]
      self.CurrentMeter:int = obj["CurrentMeter"]
      self.Hours:int = obj["Hours"]
      self.MeterUOM:str = obj["MeterUOM"]
      self.Qty:int = obj["Qty"]
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReportQtyPartRow:
   def __init__(self, obj):
      self.EmpID:str = obj["EmpID"]
      self.PartNum:str = obj["PartNum"]
      self.CurrentQty:int = obj["CurrentQty"]
      self.PrevQty:int = obj["PrevQty"]
      self.TotalQty:int = obj["TotalQty"]
      self.RequestMove:bool = obj["RequestMove"]
      self.CurrentUOM:str = obj["CurrentUOM"]
      """  Unit of measure for CurrentQty  """  
      self.PrevUOM:str = obj["PrevUOM"]
      """  Unit of measure for PrevQty  """  
      self.TotalUOM:str = obj["TotalUOM"]
      """  Unit of measure for TotalQty  """  
      self.PartDescription:str = obj["PartDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReportQtyRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.ResourceID:str = obj["ResourceID"]
      self.CurrentQty:int = obj["CurrentQty"]
      self.TotalQty:int = obj["TotalQty"]
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.OprDescription:str = obj["OprDescription"]
      self.EmpID:str = obj["EmpID"]
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.EnableReqOprTag:bool = obj["EnableReqOprTag"]
      """  Indicates whether to enable/disable the RequestMove,NextOprSeq or Tag button  """  
      self.TagType:str = obj["TagType"]
      self.TagPart:str = obj["TagPart"]
      self.TagRevisionNum:str = obj["TagRevisionNum"]
      self.TagDescription:str = obj["TagDescription"]
      self.TagIUM:str = obj["TagIUM"]
      self.TagInputWhse:str = obj["TagInputWhse"]
      self.TagInputBinNum:str = obj["TagInputBinNum"]
      self.PrevQty:int = obj["PrevQty"]
      self.ResourceIDDesc:str = obj["ResourceIDDesc"]
      self.EnableCurrentQty:bool = obj["EnableCurrentQty"]
      """  Determines if CurrentQty is available for input.  Is set to false when ReportQtyPart records exist because the quantities will be entered at the part level.  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      """  Determines if RequestMove is available for input.  """  
      self.CurrentUOM:str = obj["CurrentUOM"]
      """  Unit of measure for CurrentQty  """  
      self.PrevUOM:str = obj["PrevUOM"]
      """  Unit of measure for PrevQty  """  
      self.TotalUOM:str = obj["TotalUOM"]
      """  Unit of measure for TotalQty  """  
      self.EnableInspection:bool = obj["EnableInspection"]
      """  Enable input Inspection Data  """  
      self.Company:str = obj["Company"]
      self.EnableSN:bool = obj["EnableSN"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.ClockInDate:str = obj["ClockInDate"]
      self.ClockinTime:int = obj["ClockinTime"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.CompletedQty:int = obj["CompletedQty"]
      """  Display the quantity completed for this operation in general.  """  
      self.CompletedQtyUOM:str = obj["CompletedQtyUOM"]
      """  Unit of measure for CompletedQty  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EnablePCID:bool = obj["EnablePCID"]
      """  Internal flag used for the row rules to control whether the PCID columns should be enabled.  """  
      self.OutputBin:str = obj["OutputBin"]
      """  BinNum  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.OprSeqDescription:str = obj["OprSeqDescription"]
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.CurrentAttributeSetDescription:str = obj["CurrentAttributeSetDescription"]
      """  The Full Description of the Attribute Set for CurrentQty  """  
      self.CurrentAttributeSetID:int = obj["CurrentAttributeSetID"]
      """  he unique identifier of the related Dynamic Attribute Set for the Current Quantity.  """  
      self.CurrentAttributeSetShortDescription:str = obj["CurrentAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for CurrentQty  """  
      self.CurrentRevisionNum:str = obj["CurrentRevisionNum"]
      self.CurrentTrackInventoryByRevision:bool = obj["CurrentTrackInventoryByRevision"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReportQtyTableset:
   def __init__(self, obj):
      self.ReportQty:list[Erp_Tablesets_ReportQtyRow] = obj["ReportQty"]
      self.ReportQtyEquip:list[Erp_Tablesets_ReportQtyEquipRow] = obj["ReportQtyEquip"]
      self.ReportQtyPart:list[Erp_Tablesets_ReportQtyPartRow] = obj["ReportQtyPart"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetNewLaborEquip_input:
   """ Required : 
   empID
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Current Employee ID  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class GetNewLaborEquip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReportQty_input:
   """ Required : 
   empID
   DtlLaborHedSeq
   DtlLaborDtlSeq
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Current Employee ID  """  
      self.DtlLaborHedSeq:int = obj["DtlLaborHedSeq"]
      """  Current LaborDtl.LaborHedSeq value if record is available  """  
      self.DtlLaborDtlSeq:int = obj["DtlLaborDtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value if record is available  """  
      pass

class GetNewReportQty_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReportQtyTableset] = obj["returnObj"]
      pass

class GetSelectSerialNumbersParams_input:
   """ Required : 
   hedSeq
   dtlSeq
   ds
   """  
   def __init__(self, obj):
      self.hedSeq:int = obj["hedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.dtlSeq:int = obj["dtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangeAsmSeq_input:
   """ Required : 
   assemblySeq
   ds
   """  
   def __init__(self, obj):
      self.assemblySeq:int = obj["assemblySeq"]
      """  Assembly Sequence  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeAsmSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEquipID_input:
   """ Required : 
   equipID
   DtlLaborHedSeq
   DtlLaborDtlSeq
   ds
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  equipID  """  
      self.DtlLaborHedSeq:int = obj["DtlLaborHedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.DtlLaborDtlSeq:int = obj["DtlLaborDtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeNextOprSeq_input:
   """ Required : 
   nextOprSeq
   ds
   """  
   def __init__(self, obj):
      self.nextOprSeq:int = obj["nextOprSeq"]
      """  Next Operation Sequence  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeNextOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOprSeq_input:
   """ Required : 
   oprSeq
   ds
   """  
   def __init__(self, obj):
      self.oprSeq:int = obj["oprSeq"]
      """  Operation Sequence  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCID_input:
   """ Required : 
   pcid
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  PCID to validate  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResource_input:
   """ Required : 
   resourceID
   ds
   """  
   def __init__(self, obj):
      self.resourceID:str = obj["resourceID"]
      """  Resource ID  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class OnChangeResource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReportQuantity_input:
   """ Required : 
   hedSeq
   dtlSeq
   ds
   """  
   def __init__(self, obj):
      self.hedSeq:int = obj["hedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.dtlSeq:int = obj["dtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class ReportQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateLaborEquip_input:
   """ Required : 
   empID
   equipID
   hedSeq
   dtlSeq
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Current Employee ID  """  
      self.equipID:str = obj["equipID"]
      """  Current Labor Equipment ID  """  
      self.hedSeq:int = obj["hedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.dtlSeq:int = obj["dtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

class UpdateLaborEquip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   hedSeq
   dtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      self.hedSeq:int = obj["hedSeq"]
      """  Current LaborDtl.LaborHedSeq value  """  
      self.dtlSeq:int = obj["dtlSeq"]
      """  Current LaborDtl.LaborDtlSeq value  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class ValidateSerialBeforeSelect_input:
   """ Required : 
   ds
   dtlLaborHedSeq
   dtlLaborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      self.dtlLaborHedSeq:int = obj["dtlLaborHedSeq"]
      """  Labor Head Sequence  """  
      self.dtlLaborDtlSeq:int = obj["dtlLaborDtlSeq"]
      """  Labor Dtl Sequence  """  
      pass

class ValidateSerialBeforeSelect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReportQtyTableset] = obj["ds"]
      self.notEnoughSerials:str = obj["parameters"]
      self.totSNReq:int = obj["parameters"]
      self.totNewSNReq:int = obj["parameters"]
      pass

      """  output parameters  """  

