import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustBillToSvc
# Description: Used as a search object for CustBillTo.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustBillToes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustBillToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustBillToes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBillToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes",headers=creds) as resp:
           return await resp.json()

async def post_CustBillToes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustBillToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustBillToes_Company_CustNum_BTCustNum(Company, CustNum, BTCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustBillTo item
   Description: Calls GetByID to retrieve the CustBillTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustBillTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param BTCustNum: Desc: BTCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustBillToes_Company_CustNum_BTCustNum(Company, CustNum, BTCustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustBillTo for the service
   Description: Calls UpdateExt to update CustBillTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustBillTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param BTCustNum: Desc: BTCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustBillToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustBillToes_Company_CustNum_BTCustNum(Company, CustNum, BTCustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustBillTo item
   Description: Call UpdateExt to delete CustBillTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustBillTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param BTCustNum: Desc: BTCustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/CustBillToes(" + Company + "," + CustNum + "," + BTCustNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustBillToListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCustBillTo, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCustBillTo=" + whereClauseCustBillTo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, btCustNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "btCustNum=" + btCustNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListByBTCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByBTCustID
   Description: Calls the normal GetList but returns the list dataset with the starting at.
   OperationID: GetListByBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForReportFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForReportFilter
   Description: Retrieves the List Data Set containing CustBillTo records filtered by BTCustNum.
   OperationID: GetListForReportFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForReportFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForReportFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustBillTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustBillTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustBillTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustBillTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustBillTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustBillToSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustBillToListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustBillToRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustBillToRow] = obj["value"]
      pass

class Erp_Tablesets_CustBillToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Indicates the CustNum of the alternate Bill To Customer.  """  
      self.DefaultBillTo:bool = obj["DefaultBillTo"]
      """  Indicates whether this Alt Bill To is the default record or not.  """  
      self.InvoiceAddress:bool = obj["InvoiceAddress"]
      """  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.OurBankCode:str = obj["OurBankCode"]
      """  Our Bank Code  """  
      self.BTLegalName:str = obj["BTLegalName"]
      """  Full Legal name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BTAddress1:str = obj["BTAddress1"]
      """  BTAddress one from the Cusomer table for this AltBTCustNum.  """  
      self.BTAddress2:str = obj["BTAddress2"]
      """  BTAddress two from the Customer table for this AltBTCustNum.  """  
      self.BTAddress3:str = obj["BTAddress3"]
      """  BTAddress three from the Customer table for this AltBTCustNum.  """  
      self.BTAddrList:str = obj["BTAddrList"]
      """  The BTAddrList from the Customer table for this AltBTCustNum.  """  
      self.BTCity:str = obj["BTCity"]
      """  The BTcity from the Customer table for this AltBTCustNum.  """  
      self.BTConPrc:int = obj["BTConPrc"]
      """  Primary billing contact.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Contact name.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  The BTCountry from the Customer table for this AltBTCustNum.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  The BT Customer ID from the Customer table for this AltBTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  The BT Customer Name from the Customer table for this AltBTCustNum.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The BTFaxNum from the Customer table for this AltBTCustNum.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The BTPhoneNum from the Customer table for this AltBTCustNum.  """  
      self.BTState:str = obj["BTState"]
      """  The BTState from the Customer Table for this AltBTCustNum.  """  
      self.BTZip:str = obj["BTZip"]
      """  The BTZip from the Customer table for this AltBTCustNum.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from the Customer table for this AltBTCustNum.  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if CustBillTo is Global (Master or Linked)  """  
      self.BTCreditHold:bool = obj["BTCreditHold"]
      """  Bill to credit hold flag.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The Customer Name from the Customer table for this AltBTCustNum.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBillToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Indicates the CustNum of the alternate Bill To Customer.  """  
      self.DefaultBillTo:bool = obj["DefaultBillTo"]
      """  Indicates whether this Alt Bill To is the default record or not.  """  
      self.InvoiceAddress:bool = obj["InvoiceAddress"]
      """  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.OurBankCode:str = obj["OurBankCode"]
      """  Our Bank Code  """  
      self.BTLegalName:str = obj["BTLegalName"]
      """  Full Legal name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FSACustomerNotSent:bool = obj["FSACustomerNotSent"]
      """  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  """  
      self.BTAddress1:str = obj["BTAddress1"]
      """  BTAddress one from the Cusomer table for this AltBTCustNum.  """  
      self.BTAddress2:str = obj["BTAddress2"]
      """  BTAddress two from the Customer table for this AltBTCustNum.  """  
      self.BTAddress3:str = obj["BTAddress3"]
      """  BTAddress three from the Customer table for this AltBTCustNum.  """  
      self.BTAddrList:str = obj["BTAddrList"]
      """  The BTAddrList from the Customer table for this AltBTCustNum.  """  
      self.BTCity:str = obj["BTCity"]
      """  The BTcity from the Customer table for this AltBTCustNum.  """  
      self.BTConPrc:int = obj["BTConPrc"]
      """  Primary billing contact.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Contact name.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  The BTCountry from the Customer table for this AltBTCustNum.  """  
      self.BTCreditHold:bool = obj["BTCreditHold"]
      """  Bill to credit hold flag.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  The BT Customer ID from the Customer table for this AltBTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  The BT Customer Name from the Customer table for this AltBTCustNum.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The BTFaxNum from the Customer table for this AltBTCustNum.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The BTPhoneNum from the Customer table for this AltBTCustNum.  """  
      self.BTState:str = obj["BTState"]
      """  The BTState from the Customer Table for this AltBTCustNum.  """  
      self.BTZip:str = obj["BTZip"]
      """  The BTZip from the Customer table for this AltBTCustNum.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from the Customer table for this AltBTCustNum.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The Customer Name from the Customer table for this AltBTCustNum.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if CustBillTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  """  
      self.BTAddress:str = obj["BTAddress"]
      """  The full formatted address from the Customer table for this AltBTCustNum.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   custNum
   btCustNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.btCustNum:int = obj["btCustNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CustBillToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Indicates the CustNum of the alternate Bill To Customer.  """  
      self.DefaultBillTo:bool = obj["DefaultBillTo"]
      """  Indicates whether this Alt Bill To is the default record or not.  """  
      self.InvoiceAddress:bool = obj["InvoiceAddress"]
      """  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.OurBankCode:str = obj["OurBankCode"]
      """  Our Bank Code  """  
      self.BTLegalName:str = obj["BTLegalName"]
      """  Full Legal name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BTAddress1:str = obj["BTAddress1"]
      """  BTAddress one from the Cusomer table for this AltBTCustNum.  """  
      self.BTAddress2:str = obj["BTAddress2"]
      """  BTAddress two from the Customer table for this AltBTCustNum.  """  
      self.BTAddress3:str = obj["BTAddress3"]
      """  BTAddress three from the Customer table for this AltBTCustNum.  """  
      self.BTAddrList:str = obj["BTAddrList"]
      """  The BTAddrList from the Customer table for this AltBTCustNum.  """  
      self.BTCity:str = obj["BTCity"]
      """  The BTcity from the Customer table for this AltBTCustNum.  """  
      self.BTConPrc:int = obj["BTConPrc"]
      """  Primary billing contact.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Contact name.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  The BTCountry from the Customer table for this AltBTCustNum.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  The BT Customer ID from the Customer table for this AltBTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  The BT Customer Name from the Customer table for this AltBTCustNum.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The BTFaxNum from the Customer table for this AltBTCustNum.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The BTPhoneNum from the Customer table for this AltBTCustNum.  """  
      self.BTState:str = obj["BTState"]
      """  The BTState from the Customer Table for this AltBTCustNum.  """  
      self.BTZip:str = obj["BTZip"]
      """  The BTZip from the Customer table for this AltBTCustNum.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from the Customer table for this AltBTCustNum.  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if CustBillTo is Global (Master or Linked)  """  
      self.BTCreditHold:bool = obj["BTCreditHold"]
      """  Bill to credit hold flag.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The Customer Name from the Customer table for this AltBTCustNum.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBillToListTableset:
   def __init__(self, obj):
      self.CustBillToList:list[Erp_Tablesets_CustBillToListRow] = obj["CustBillToList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustBillToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Indicates the CustNum of the alternate Bill To Customer.  """  
      self.DefaultBillTo:bool = obj["DefaultBillTo"]
      """  Indicates whether this Alt Bill To is the default record or not.  """  
      self.InvoiceAddress:bool = obj["InvoiceAddress"]
      """  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.OurBankCode:str = obj["OurBankCode"]
      """  Our Bank Code  """  
      self.BTLegalName:str = obj["BTLegalName"]
      """  Full Legal name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FSACustomerNotSent:bool = obj["FSACustomerNotSent"]
      """  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  """  
      self.BTAddress1:str = obj["BTAddress1"]
      """  BTAddress one from the Cusomer table for this AltBTCustNum.  """  
      self.BTAddress2:str = obj["BTAddress2"]
      """  BTAddress two from the Customer table for this AltBTCustNum.  """  
      self.BTAddress3:str = obj["BTAddress3"]
      """  BTAddress three from the Customer table for this AltBTCustNum.  """  
      self.BTAddrList:str = obj["BTAddrList"]
      """  The BTAddrList from the Customer table for this AltBTCustNum.  """  
      self.BTCity:str = obj["BTCity"]
      """  The BTcity from the Customer table for this AltBTCustNum.  """  
      self.BTConPrc:int = obj["BTConPrc"]
      """  Primary billing contact.  """  
      self.BTContactName:str = obj["BTContactName"]
      """  Contact name.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  The BTCountry from the Customer table for this AltBTCustNum.  """  
      self.BTCreditHold:bool = obj["BTCreditHold"]
      """  Bill to credit hold flag.  """  
      self.BTCustID:str = obj["BTCustID"]
      """  The BT Customer ID from the Customer table for this AltBTCustNum.  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  The BT Customer Name from the Customer table for this AltBTCustNum.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The BTFaxNum from the Customer table for this AltBTCustNum.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The BTPhoneNum from the Customer table for this AltBTCustNum.  """  
      self.BTState:str = obj["BTState"]
      """  The BTState from the Customer Table for this AltBTCustNum.  """  
      self.BTZip:str = obj["BTZip"]
      """  The BTZip from the Customer table for this AltBTCustNum.  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID from the Customer table for this AltBTCustNum.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The Customer Name from the Customer table for this AltBTCustNum.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if CustBillTo is Global (Master or Linked)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbCustNum and GlbBTCustNum that is linking to this CustBillTo  """  
      self.BTAddress:str = obj["BTAddress"]
      """  The full formatted address from the Customer table for this AltBTCustNum.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustBillToTableset:
   def __init__(self, obj):
      self.CustBillTo:list[Erp_Tablesets_CustBillToRow] = obj["CustBillTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCustBillToTableset:
   def __init__(self, obj):
      self.CustBillTo:list[Erp_Tablesets_CustBillToRow] = obj["CustBillTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   btCustNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.btCustNum:int = obj["btCustNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBillToTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBillToTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBillToTableset] = obj["returnObj"]
      pass

class GetListByBTCustID_input:
   """ Required : 
   custNum
   btCustID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Sold to customer number.  """  
      self.btCustID:str = obj["btCustID"]
      """  BTCustID to start at and sort by.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListByBTCustID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBillToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListForReportFilter_input:
   """ Required : 
   customers
   """  
   def __init__(self, obj):
      self.customers:str = obj["customers"]
      """  List of customers separated by '~'.  """  
      pass

class GetListForReportFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBillToListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustBillToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustBillTo_input:
   """ Required : 
   ds
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustBillToTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewCustBillTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustBillToTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCustBillTo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCustBillTo:str = obj["whereClauseCustBillTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustBillToTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustBillToTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustBillToTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustBillToTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustBillToTableset] = obj["ds"]
      pass

      """  output parameters  """  

