import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SNTranSearchSvc
# Description: Serial Number Transaction Search Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SNTranSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNTranSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches",headers=creds) as resp:
           return await resp.json()

async def post_SNTranSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNTranSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company, PartNum, SerialNumber, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNTranSearch item
   Description: Calls GetByID to retrieve the SNTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company, PartNum, SerialNumber, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNTranSearch for the service
   Description: Calls UpdateExt to update SNTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNTranSearches_Company_PartNum_SerialNumber_TranNum(Company, PartNum, SerialNumber, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNTranSearch item
   Description: Call UpdateExt to delete SNTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/SNTranSearches(" + Company + "," + PartNum + "," + SerialNumber + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSNTran, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNTran=" + whereClauseSNTran
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, serialNumber, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serialNumber=" + serialNumber
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSNTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSNTran
   Description: Purpose:     Get all rows from the SNTran that has a TranType = 'RMA-INS'";
Parameters:  int rmaNum, int rmaLine, int rmaReceiptNum
Notes:       If a SN has more than one row in SNTran with TranType = 'RMA-INS', selects the row with the most recent TranNum.
   OperationID: GetSNTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSNTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSNTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSNTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSNTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSNTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSNTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSNTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SNTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNTranRow] = obj["value"]
      pass

class Erp_Tablesets_SNTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  The serial number of the part that this transaction is for.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow for a unique key for the file.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing slip line that this record is associated with.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call that this record is accociated with.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call line that this record is accociated with.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA that this record is accociated with.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA detail that this record is accociated with.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.TranDate:str = obj["TranDate"]
      """  The date of the tranaction  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.SysDate:str = obj["SysDate"]
      """  System Date  """  
      self.SysTime:int = obj["SysTime"]
      """  System time  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Assembly Sequence  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  TFOrdNum  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  TFOrdLine  """  
      self.DispSysTime:str = obj["DispSysTime"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  The serial number of the part that this transaction is for.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow for a unique key for the file.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing slip line that this record is associated with.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call that this record is accociated with.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call line that this record is accociated with.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA that this record is accociated with.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA detail that this record is accociated with.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.TranDate:str = obj["TranDate"]
      """  The date of the tranaction  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.SysDate:str = obj["SysDate"]
      """  System Date  """  
      self.SysTime:int = obj["SysTime"]
      """  System time  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Assembly Sequence  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  FSAssetClassCode  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  FSServiceLevelAgreement  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.MeterReading:int = obj["MeterReading"]
      """  MeterReading  """  
      self.OTS:bool = obj["OTS"]
      """  One time shipto flag  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTS Address 1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTS Address 2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTS Address 3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTS City  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTS Contact  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTS Country Number  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTS Country Number  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  One Time fax number  """  
      self.OTSName:str = obj["OTSName"]
      """  OTS Name  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTS Phone Number  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTS Resale ID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS Ship To Num  """  
      self.OTSState:str = obj["OTSState"]
      """  OTS State  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Region Code  """  
      self.OTSZip:str = obj["OTSZip"]
      """  OTS Zip  """  
      self.PriorJobNum:str = obj["PriorJobNum"]
      """  PriorJobNum  """  
      self.PriorAssemblySeq:int = obj["PriorAssemblySeq"]
      """  PriorAssemblySeq  """  
      self.PriorMtlSeq:int = obj["PriorMtlSeq"]
      """  PriorMtlSeq  """  
      self.PriorPartNum:str = obj["PriorPartNum"]
      """  PriorPartNum  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.MscPackNum:int = obj["MscPackNum"]
      """  MscPackNum  """  
      self.MscPackLine:int = obj["MscPackLine"]
      """  MscPackLine  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. When the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  TFOrdNum  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  TFOrdLine  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SerialNumberSNStatus:str = obj["SerialNumberSNStatus"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   serialNumber
   tranNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SNTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  The serial number of the part that this transaction is for.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow for a unique key for the file.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing slip line that this record is associated with.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call that this record is accociated with.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call line that this record is accociated with.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA that this record is accociated with.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA detail that this record is accociated with.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.TranDate:str = obj["TranDate"]
      """  The date of the tranaction  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.SysDate:str = obj["SysDate"]
      """  System Date  """  
      self.SysTime:int = obj["SysTime"]
      """  System time  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Assembly Sequence  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  TFOrdNum  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  TFOrdLine  """  
      self.DispSysTime:str = obj["DispSysTime"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNTranListTableset:
   def __init__(self, obj):
      self.SNTranList:list[Erp_Tablesets_SNTranListRow] = obj["SNTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SNTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  The serial number of the part that this transaction is for.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow for a unique key for the file.  """  
      self.TranType:str = obj["TranType"]
      """  Field that indicates the type of transaction  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  Packing slip line that this record is associated with.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call that this record is accociated with.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call line that this record is accociated with.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA that this record is accociated with.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA detail that this record is accociated with.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person  """  
      self.TranDate:str = obj["TranDate"]
      """  The date of the tranaction  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  The job number that this item is linked to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the Assembly record within the JobNum/LotNum. This can be user assigned or assigned by the system. The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackSlipLine:int = obj["PackSlipLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  A Standard prefix that will be attached to all Serial Numbers for a particular part.  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Format of the Base number.  """  
      self.SNBaseStructure:str = obj["SNBaseStructure"]
      """  Information about serail number formatting.  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number of Serial Number, needed mainly for adding ranges of numbers.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred.  """  
      self.SNReference:str = obj["SNReference"]
      """  A generic fill-in field that could be used to allow the user to enter data.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA receipt  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  """  
      self.SysDate:str = obj["SysDate"]
      """  System Date  """  
      self.SysTime:int = obj["SysTime"]
      """  System time  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.WarrExpiration:str = obj["WarrExpiration"]
      """  The latest of the 3 warranty expiration dates  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.NonConfNum:int = obj["NonConfNum"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Order packing slip.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Order packing slip line.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Related (OrderHed) Sales Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related (OrderDtl) sales order line number  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  related (OrderRel) order release number  """  
      self.PrevSNStatus:str = obj["PrevSNStatus"]
      """  The status of this serial numbered item prior to its current status.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Used to tie back to the related RMADisp record.  """  
      self.ShippedFrom:str = obj["ShippedFrom"]
      """  Indicates where the serial#  was shipped from, (I)nventory or (W)ip.  """  
      self.SNStatus:str = obj["SNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.Voided:bool = obj["Voided"]
      """  Indicates that this serial number has been voided.  """  
      self.FullyMatched:bool = obj["FullyMatched"]
      """  This flag will indicate whether the lower level serial numbers have been fully matched for a parent serial created by a job.  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a mask was being used where characters were stripped (using ~ in the mask).  """  
      self.SNMask:str = obj["SNMask"]
      """  The Serial Mask ID that was used when a serial number was created.  """  
      self.AddedByMatching:bool = obj["AddedByMatching"]
      """  Indicates that this child serial number was manually added in the Serial Matching UI using the New Child Part option as opposed to being generated based on Job or Part BOM.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  The suffix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number ? currently used only by SNBaseStructure Mask types  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Indicates that this serial numbered item has been scrapped.  """  
      self.DMRActionNum:int = obj["DMRActionNum"]
      """  DMR action number.  """  
      self.FailSelect:bool = obj["FailSelect"]
      """  Indicates that this item has failed inspection.  """  
      self.LineDetailNum:int = obj["LineDetailNum"]
      """  Identifies the contract record along with Company, contractNum, ContractLine.  """  
      self.TranAdd:bool = obj["TranAdd"]
      """  Added at shipment  """  
      self.SubConOprSeq:int = obj["SubConOprSeq"]
      """  When the serial number is shipped by Subcontract Shipment this field holds the JobOper.OprSeq the shipment was made for.  """  
      self.ScrapLaborHedSeq:int = obj["ScrapLaborHedSeq"]
      """  The LaborHedSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.ScrapLaborDtlSeq:int = obj["ScrapLaborDtlSeq"]
      """  The LaborDtlSeq for the last LaborDtl that  Scrapped, completed or send the serial number to  nonconf when booking labor against a job operation  """  
      self.LastLbrOprSeq:int = obj["LastLbrOprSeq"]
      """  The last OperSeq in Labor entry where this serial number was flagged as completed.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNumber assigned to the serial number in cycle count/Physical Inventory.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.NextLbrOprSeq:int = obj["NextLbrOprSeq"]
      """  Next Labor Operation Sequence  """  
      self.NextLbrAssySeq:int = obj["NextLbrAssySeq"]
      """  Next Labor Assembly Sequence  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.Latitude:int = obj["Latitude"]
      """  Latitude  """  
      self.Longitude:int = obj["Longitude"]
      """  Longitude  """  
      self.Altitude:int = obj["Altitude"]
      """  Altitude  """  
      self.FSAssetClassCode:str = obj["FSAssetClassCode"]
      """  FSAssetClassCode  """  
      self.FSServiceLevelAgreement:str = obj["FSServiceLevelAgreement"]
      """  FSServiceLevelAgreement  """  
      self.Accuracy:int = obj["Accuracy"]
      """  Accuracy  """  
      self.MeterReading:int = obj["MeterReading"]
      """  MeterReading  """  
      self.OTS:bool = obj["OTS"]
      """  One time shipto flag  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTS Address 1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTS Address 2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTS Address 3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTS City  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTS Contact  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTS Country Number  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTS Country Number  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  One Time fax number  """  
      self.OTSName:str = obj["OTSName"]
      """  OTS Name  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTS Phone Number  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTS Resale ID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  CustID to be used if the OTS is used to create a customer record.  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTS Ship To Num  """  
      self.OTSState:str = obj["OTSState"]
      """  OTS State  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTS Tax Region Code  """  
      self.OTSZip:str = obj["OTSZip"]
      """  OTS Zip  """  
      self.PriorJobNum:str = obj["PriorJobNum"]
      """  PriorJobNum  """  
      self.PriorAssemblySeq:int = obj["PriorAssemblySeq"]
      """  PriorAssemblySeq  """  
      self.PriorMtlSeq:int = obj["PriorMtlSeq"]
      """  PriorMtlSeq  """  
      self.PriorPartNum:str = obj["PriorPartNum"]
      """  PriorPartNum  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.MscPackNum:int = obj["MscPackNum"]
      """  MscPackNum  """  
      self.MscPackLine:int = obj["MscPackLine"]
      """  MscPackLine  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Identifier of the asset this Serial Number is associated to. When the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Addition Number of the asset the Serial Number is associated to. when the SNStatus = INVENTORY this means the SN has been selected for an Asset Addition that has not yet been posted.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  DisposalNum  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the serial number has to be synchronized with Epicor FSA application.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  TFOrdNum  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  TFOrdLine  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SerialNumberSNStatus:str = obj["SerialNumberSNStatus"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNTranSearchTableset:
   def __init__(self, obj):
      self.SNTran:list[Erp_Tablesets_SNTranRow] = obj["SNTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSNTranSearchTableset:
   def __init__(self, obj):
      self.SNTran:list[Erp_Tablesets_SNTranRow] = obj["SNTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   serialNumber
   tranNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranSearchTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSNTran_input:
   """ Required : 
   ds
   partNum
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SNTranSearchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.serialNumber:str = obj["serialNumber"]
      pass

class GetNewSNTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SNTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSNTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSNTran:str = obj["whereClauseSNTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSNTran_input:
   """ Required : 
   rmaNum
   rmaLine
   rmaReceiptNum
   """  
   def __init__(self, obj):
      self.rmaNum:int = obj["rmaNum"]
      self.rmaLine:int = obj["rmaLine"]
      self.rmaReceiptNum:int = obj["rmaReceiptNum"]
      pass

class GetSNTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SNTranSearchTableset] = obj["returnObj"]
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSNTranSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSNTranSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SNTranSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SNTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

