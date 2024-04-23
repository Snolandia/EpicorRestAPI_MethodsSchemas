import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RebateTransSvc
# Description: This is the maintenance program for RebateTrans records
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RebateTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RebateTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RebateTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans",headers=creds) as resp:
           return await resp.json()

async def post_RebateTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company, RebateID, LineNum, CustNum, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RebateTran item
   Description: Calls GetByID to retrieve the RebateTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RebateTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company, RebateID, LineNum, CustNum, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RebateTran for the service
   Description: Calls UpdateExt to update RebateTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RebateTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RebateTransRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RebateTrans_Company_RebateID_LineNum_CustNum_TranNum(Company, RebateID, LineNum, CustNum, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RebateTran item
   Description: Call UpdateExt to delete RebateTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RebateTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RebateID: Desc: RebateID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/RebateTrans(" + Company + "," + RebateID + "," + LineNum + "," + CustNum + "," + TranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RebateTransListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRebateTrans, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRebateTrans=" + whereClauseRebateTrans
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rebateID, lineNum, custNum, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "rebateID=" + rebateID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lineNum=" + lineNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAll
   Description: This method deletes all the selected rebate transactions.
   OperationID: DeleteAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportRebateTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportRebateTrans
   Description: Call this method to import rebate transactions into the database.
This method expects an input data table ttImportRebateTrans with data coming
from an external comma delimited file.
   OperationID: ImportRebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportRebateTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportRebateTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportFile
   OperationID: ImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRebateTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRebateTrans
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRebateTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRebateTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRebateTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RebateTransSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateTransListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RebateTransRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RebateTransRow] = obj["value"]
      pass

class Erp_Tablesets_RebateTransListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date Created  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Date of the source transaction  """  
      self.Quantity:int = obj["Quantity"]
      """  Invoiced Quantity  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity Unit of Measure  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.DocRebateAmount:int = obj["DocRebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.Adjustments:int = obj["Adjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.DocAdjustments:int = obj["DocAdjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  """  
      self.Applied:bool = obj["Applied"]
      """  Indicates that this transaction has been applied against a rebate payment  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.SalesDept:str = obj["SalesDept"]
      """   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  """  
      self.SalesDiv:str = obj["SalesDiv"]
      """   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice transaction is associated with (Payment)  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice transaction is associated with (Credit Memo)  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.Rpt1Adjustments:int = obj["Rpt1Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt2Adjustments:int = obj["Rpt2Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt3Adjustments:int = obj["Rpt3Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1RebateAmount:int = obj["Rpt1RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2RebateAmount:int = obj["Rpt2RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3RebateAmount:int = obj["Rpt3RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetRebateAmt:int = obj["NetRebateAmt"]
      self.PartUOM:str = obj["PartUOM"]
      """  Part UOM  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      """  Full description of Product Group.  """  
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      """  Unit of Measure  """  
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      """  A unique part number that identifies this part.  """  
      self.RebateHdrRebateDesc:str = obj["RebateHdrRebateDesc"]
      """  Rebate Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date Created  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Date of the source transaction  """  
      self.Quantity:int = obj["Quantity"]
      """  Invoiced Quantity  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity Unit of Measure  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.DocRebateAmount:int = obj["DocRebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.Adjustments:int = obj["Adjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.DocAdjustments:int = obj["DocAdjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  """  
      self.Applied:bool = obj["Applied"]
      """  Indicates that this transaction has been applied against a rebate payment  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.SalesDept:str = obj["SalesDept"]
      """   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  """  
      self.SalesDiv:str = obj["SalesDiv"]
      """   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice transaction is associated with (Payment)  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice transaction is associated with (Credit Memo)  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.Rpt1Adjustments:int = obj["Rpt1Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt2Adjustments:int = obj["Rpt2Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt3Adjustments:int = obj["Rpt3Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1RebateAmount:int = obj["Rpt1RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2RebateAmount:int = obj["Rpt2RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3RebateAmount:int = obj["Rpt3RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetRebateAmt:int = obj["NetRebateAmt"]
      self.PartUOM:str = obj["PartUOM"]
      """  Part UOM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      self.RebateHdrRebateDesc:str = obj["RebateHdrRebateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteAll_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

class DeleteAll_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rebateID
   lineNum
   custNum
   tranNum
   """  
   def __init__(self, obj):
      self.rebateID:str = obj["rebateID"]
      self.lineNum:int = obj["lineNum"]
      self.custNum:int = obj["custNum"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ImportRebateTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RebateID:str = obj["RebateID"]
      self.LineNum:int = obj["LineNum"]
      self.CustID:str = obj["CustID"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.Quantity:int = obj["Quantity"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.Discount:int = obj["Discount"]
      self.RebateAmount:int = obj["RebateAmount"]
      self.Adjustments:int = obj["Adjustments"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      self.Void:bool = obj["Void"]
      self.Applied:bool = obj["Applied"]
      """  Has been applied to a payment or credit memo  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      self.DocRebateAmount:int = obj["DocRebateAmount"]
      self.DocAdjustments:int = obj["DocAdjustments"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.RefCode:str = obj["RefCode"]
      self.DocToRef:bool = obj["DocToRef"]
      self.RefToBase:bool = obj["RefToBase"]
      self.RefToBaseRate:int = obj["RefToBaseRate"]
      self.SalesDept:str = obj["SalesDept"]
      self.SalesDiv:str = obj["SalesDiv"]
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      self.PartNum:str = obj["PartNum"]
      self.ProdCode:str = obj["ProdCode"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportRebateTransTableset:
   def __init__(self, obj):
      self.ImportRebateTrans:list[Erp_Tablesets_ImportRebateTransRow] = obj["ImportRebateTrans"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RebateTransListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date Created  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Date of the source transaction  """  
      self.Quantity:int = obj["Quantity"]
      """  Invoiced Quantity  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity Unit of Measure  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.DocRebateAmount:int = obj["DocRebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.Adjustments:int = obj["Adjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.DocAdjustments:int = obj["DocAdjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  """  
      self.Applied:bool = obj["Applied"]
      """  Indicates that this transaction has been applied against a rebate payment  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.SalesDept:str = obj["SalesDept"]
      """   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  """  
      self.SalesDiv:str = obj["SalesDiv"]
      """   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice transaction is associated with (Payment)  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice transaction is associated with (Credit Memo)  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.Rpt1Adjustments:int = obj["Rpt1Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt2Adjustments:int = obj["Rpt2Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt3Adjustments:int = obj["Rpt3Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1RebateAmount:int = obj["Rpt1RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2RebateAmount:int = obj["Rpt2RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3RebateAmount:int = obj["Rpt3RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetRebateAmt:int = obj["NetRebateAmt"]
      self.PartUOM:str = obj["PartUOM"]
      """  Part UOM  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      """  Full description of Product Group.  """  
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      """  Unit of Measure  """  
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      """  A unique part number that identifies this part.  """  
      self.RebateHdrRebateDesc:str = obj["RebateHdrRebateDesc"]
      """  Rebate Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateTransListTableset:
   def __init__(self, obj):
      self.RebateTransList:list[Erp_Tablesets_RebateTransListRow] = obj["RebateTransList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RebateTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RebateID:str = obj["RebateID"]
      """  Unique Identifier for the Rebate  """  
      self.LineNum:int = obj["LineNum"]
      """  Internal unique identifier for the RebateDtl table  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date Created  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Date of the source transaction  """  
      self.Quantity:int = obj["Quantity"]
      """  Invoiced Quantity  """  
      self.QuantityUOM:str = obj["QuantityUOM"]
      """  Quantity Unit of Measure  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.RebateAmount:int = obj["RebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.DocRebateAmount:int = obj["DocRebateAmount"]
      """  Amount of Rebate Earned for this transaction (calculated)  """  
      self.Adjustments:int = obj["Adjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.DocAdjustments:int = obj["DocAdjustments"]
      """  Adjustments to the calculated Rebate Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.Void:bool = obj["Void"]
      """  Indicates if the transaction has been reviewed and is not valid for the Rebate.  If the transaction is deleted, the next generate process will re-create it.  """  
      self.Applied:bool = obj["Applied"]
      """  Indicates that this transaction has been applied against a rebate payment  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.SalesDept:str = obj["SalesDept"]
      """   Department component of the default Sales G/L account for the item being invoiced.
See SalesDiv field description for related info.  """  
      self.SalesDiv:str = obj["SalesDiv"]
      """   Division of Account  component for the default Sales G/L account.
See SalesDiv field description for related info.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  AP Invoice transaction is associated with (Payment)  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  AR Invoice transaction is associated with (Credit Memo)  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master. Can't be blank. Used as a foreign key in other files and may be used in displays/reports where space for the full description is not available.  """  
      self.APInvoiceLine:int = obj["APInvoiceLine"]
      """  This field along with Company, VendorNum and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the APInvDtl record for the Invoice and the adding 1 to it.  """  
      self.ARInvoiceLine:int = obj["ARInvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.Rpt1Adjustments:int = obj["Rpt1Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt2Adjustments:int = obj["Rpt2Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt3Adjustments:int = obj["Rpt3Adjustments"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1RebateAmount:int = obj["Rpt1RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2RebateAmount:int = obj["Rpt2RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3RebateAmount:int = obj["Rpt3RebateAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NetRebateAmt:int = obj["NetRebateAmt"]
      self.PartUOM:str = obj["PartUOM"]
      """  Part UOM  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.ProdGrupDescription:str = obj["ProdGrupDescription"]
      self.RebateDtlPartNum:str = obj["RebateDtlPartNum"]
      self.RebateDtlProdCode:str = obj["RebateDtlProdCode"]
      self.RebateDtlUOMCode:str = obj["RebateDtlUOMCode"]
      self.RebateHdrRebateDesc:str = obj["RebateHdrRebateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RebateTransTableset:
   def __init__(self, obj):
      self.RebateTrans:list[Erp_Tablesets_RebateTransRow] = obj["RebateTrans"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRebateTransTableset:
   def __init__(self, obj):
      self.RebateTrans:list[Erp_Tablesets_RebateTransRow] = obj["RebateTrans"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   rebateID
   lineNum
   custNum
   tranNum
   """  
   def __init__(self, obj):
      self.rebateID:str = obj["rebateID"]
      self.lineNum:int = obj["lineNum"]
      self.custNum:int = obj["custNum"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTransTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateTransTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateTransTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RebateTransListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRebateTrans_input:
   """ Required : 
   ds
   rebateID
   lineNum
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      self.rebateID:str = obj["rebateID"]
      self.lineNum:int = obj["lineNum"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewRebateTrans_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRebateTrans
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRebateTrans:str = obj["whereClauseRebateTrans"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTransTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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

class ImportFile_input:
   """ Required : 
   fileName
   ds
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

class ImportFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportRebateTrans_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportRebateTransTableset] = obj["ds"]
      pass

class ImportRebateTrans_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RebateTransTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportRebateTransTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRebateTransTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRebateTransTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RebateTransTableset] = obj["ds"]
      pass

      """  output parameters  """  

