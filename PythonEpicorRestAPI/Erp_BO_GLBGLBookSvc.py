import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBGLBookSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBGLBooks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBGLBooks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBGLBooks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBGLBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/GLBGLBooks",headers=creds) as resp:
           return await resp.json()

async def post_GLBGLBooks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBGLBooks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBGLBookRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBGLBookRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/GLBGLBooks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBGLBooks_Company_ExtCompanyID_BookID(Company, ExtCompanyID, BookID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBGLBook item
   Description: Calls GetByID to retrieve the GLBGLBook item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBGLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBGLBookRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/GLBGLBooks(" + Company + "," + ExtCompanyID + "," + BookID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBGLBooks_Company_ExtCompanyID_BookID(Company, ExtCompanyID, BookID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBGLBook for the service
   Description: Calls UpdateExt to update GLBGLBook. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBGLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBGLBookRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/GLBGLBooks(" + Company + "," + ExtCompanyID + "," + BookID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBGLBooks_Company_ExtCompanyID_BookID(Company, ExtCompanyID, BookID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBGLBook item
   Description: Call UpdateExt to delete GLBGLBook item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBGLBook
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/GLBGLBooks(" + Company + "," + ExtCompanyID + "," + BookID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBGLBookListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBGLBook, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLBGLBook=" + whereClauseGLBGLBook
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extCompanyID, bookID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "bookID=" + bookID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBGLBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBGLBook
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLBookSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLBookListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBGLBookListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLBookRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBGLBookRow] = obj["value"]
      pass

class Erp_Tablesets_GLBGLBookListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndAccount:str = obj["RndAccount"]
      self.RndSegValue1:str = obj["RndSegValue1"]
      self.RndSegValue10:str = obj["RndSegValue10"]
      self.RndSegValue11:str = obj["RndSegValue11"]
      self.RndSegValue12:str = obj["RndSegValue12"]
      self.RndSegValue13:str = obj["RndSegValue13"]
      self.RndSegValue14:str = obj["RndSegValue14"]
      self.RndSegValue15:str = obj["RndSegValue15"]
      self.RndSegValue16:str = obj["RndSegValue16"]
      self.RndSegValue17:str = obj["RndSegValue17"]
      self.RndSegValue18:str = obj["RndSegValue18"]
      self.RndSegValue19:str = obj["RndSegValue19"]
      self.RndSegValue2:str = obj["RndSegValue2"]
      self.RndSegValue20:str = obj["RndSegValue20"]
      self.RndSegValue3:str = obj["RndSegValue3"]
      self.RndSegValue4:str = obj["RndSegValue4"]
      self.RndSegValue5:str = obj["RndSegValue5"]
      self.RndSegValue6:str = obj["RndSegValue6"]
      self.RndSegValue7:str = obj["RndSegValue7"]
      self.RndSegValue8:str = obj["RndSegValue8"]
      self.RndSegValue9:str = obj["RndSegValue9"]
      self.RndTolerance:int = obj["RndTolerance"]
      self.CorrAccounting:bool = obj["CorrAccounting"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBGLBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndAccount:str = obj["RndAccount"]
      self.RndSegValue1:str = obj["RndSegValue1"]
      self.RndSegValue10:str = obj["RndSegValue10"]
      self.RndSegValue11:str = obj["RndSegValue11"]
      self.RndSegValue12:str = obj["RndSegValue12"]
      self.RndSegValue13:str = obj["RndSegValue13"]
      self.RndSegValue14:str = obj["RndSegValue14"]
      self.RndSegValue15:str = obj["RndSegValue15"]
      self.RndSegValue16:str = obj["RndSegValue16"]
      self.RndSegValue17:str = obj["RndSegValue17"]
      self.RndSegValue18:str = obj["RndSegValue18"]
      self.RndSegValue19:str = obj["RndSegValue19"]
      self.RndSegValue2:str = obj["RndSegValue2"]
      self.RndSegValue20:str = obj["RndSegValue20"]
      self.RndSegValue3:str = obj["RndSegValue3"]
      self.RndSegValue4:str = obj["RndSegValue4"]
      self.RndSegValue5:str = obj["RndSegValue5"]
      self.RndSegValue6:str = obj["RndSegValue6"]
      self.RndSegValue7:str = obj["RndSegValue7"]
      self.RndSegValue8:str = obj["RndSegValue8"]
      self.RndSegValue9:str = obj["RndSegValue9"]
      self.RndTolerance:int = obj["RndTolerance"]
      self.CorrAccounting:bool = obj["CorrAccounting"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extCompanyID
   bookID
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.bookID:str = obj["bookID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLBGLBookListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndAccount:str = obj["RndAccount"]
      self.RndSegValue1:str = obj["RndSegValue1"]
      self.RndSegValue10:str = obj["RndSegValue10"]
      self.RndSegValue11:str = obj["RndSegValue11"]
      self.RndSegValue12:str = obj["RndSegValue12"]
      self.RndSegValue13:str = obj["RndSegValue13"]
      self.RndSegValue14:str = obj["RndSegValue14"]
      self.RndSegValue15:str = obj["RndSegValue15"]
      self.RndSegValue16:str = obj["RndSegValue16"]
      self.RndSegValue17:str = obj["RndSegValue17"]
      self.RndSegValue18:str = obj["RndSegValue18"]
      self.RndSegValue19:str = obj["RndSegValue19"]
      self.RndSegValue2:str = obj["RndSegValue2"]
      self.RndSegValue20:str = obj["RndSegValue20"]
      self.RndSegValue3:str = obj["RndSegValue3"]
      self.RndSegValue4:str = obj["RndSegValue4"]
      self.RndSegValue5:str = obj["RndSegValue5"]
      self.RndSegValue6:str = obj["RndSegValue6"]
      self.RndSegValue7:str = obj["RndSegValue7"]
      self.RndSegValue8:str = obj["RndSegValue8"]
      self.RndSegValue9:str = obj["RndSegValue9"]
      self.RndTolerance:int = obj["RndTolerance"]
      self.CorrAccounting:bool = obj["CorrAccounting"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBGLBookListTableset:
   def __init__(self, obj):
      self.GLBGLBookList:list[Erp_Tablesets_GLBGLBookListRow] = obj["GLBGLBookList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBGLBookRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.Description:str = obj["Description"]
      """  Descripiton of Book  """  
      self.MainBook:bool = obj["MainBook"]
      """  Indicates if this is the Main Book.  Only one main book is allowed.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookType:int = obj["BookType"]
      """  Indicates the type of book.  Standard, Consolidation, etc.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the book is inactive  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Identifier for the Fiscal Calendar assigned to the book  """  
      self.COABalFmtChg:bool = obj["COABalFmtChg"]
      """  Indiates if the blaance account structure has changed on the COA.  Yes indicates it has changed and the balance rebuild utility needs to run.  This field is used internally and is not intended for end-user use.  """  
      self.REAccount:str = obj["REAccount"]
      """  Retained Earnings Account.  May be actual account or a mask  """  
      self.RESegValue1:str = obj["RESegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.RESegValue2:str = obj["RESegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.RESegValue3:str = obj["RESegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.RESegValue4:str = obj["RESegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.RESegValue5:str = obj["RESegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.RESegValue6:str = obj["RESegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.RESegValue7:str = obj["RESegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.RESegValue8:str = obj["RESegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.RESegValue9:str = obj["RESegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.RESegValue10:str = obj["RESegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.RESegValue11:str = obj["RESegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.RESegValue12:str = obj["RESegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.RESegValue13:str = obj["RESegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.RESegValue14:str = obj["RESegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.RESegValue15:str = obj["RESegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.RESegValue16:str = obj["RESegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.RESegValue17:str = obj["RESegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.RESegValue18:str = obj["RESegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.RESegValue19:str = obj["RESegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.RESegValue20:str = obj["RESegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.RndAccount:str = obj["RndAccount"]
      self.RndSegValue1:str = obj["RndSegValue1"]
      self.RndSegValue10:str = obj["RndSegValue10"]
      self.RndSegValue11:str = obj["RndSegValue11"]
      self.RndSegValue12:str = obj["RndSegValue12"]
      self.RndSegValue13:str = obj["RndSegValue13"]
      self.RndSegValue14:str = obj["RndSegValue14"]
      self.RndSegValue15:str = obj["RndSegValue15"]
      self.RndSegValue16:str = obj["RndSegValue16"]
      self.RndSegValue17:str = obj["RndSegValue17"]
      self.RndSegValue18:str = obj["RndSegValue18"]
      self.RndSegValue19:str = obj["RndSegValue19"]
      self.RndSegValue2:str = obj["RndSegValue2"]
      self.RndSegValue20:str = obj["RndSegValue20"]
      self.RndSegValue3:str = obj["RndSegValue3"]
      self.RndSegValue4:str = obj["RndSegValue4"]
      self.RndSegValue5:str = obj["RndSegValue5"]
      self.RndSegValue6:str = obj["RndSegValue6"]
      self.RndSegValue7:str = obj["RndSegValue7"]
      self.RndSegValue8:str = obj["RndSegValue8"]
      self.RndSegValue9:str = obj["RndSegValue9"]
      self.RndTolerance:int = obj["RndTolerance"]
      self.CorrAccounting:bool = obj["CorrAccounting"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBGLBookTableset:
   def __init__(self, obj):
      self.GLBGLBook:list[Erp_Tablesets_GLBGLBookRow] = obj["GLBGLBook"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLBGLBookTableset:
   def __init__(self, obj):
      self.GLBGLBook:list[Erp_Tablesets_GLBGLBookRow] = obj["GLBGLBook"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extCompanyID
   bookID
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.bookID:str = obj["bookID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBGLBookTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBGLBookTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBGLBookTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBGLBookListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBGLBook_input:
   """ Required : 
   ds
   extCompanyID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLBookTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class GetNewGLBGLBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBGLBook
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBGLBook:str = obj["whereClauseGLBGLBook"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBGLBookTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLBGLBookTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBGLBookTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLBookTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLBookTableset] = obj["ds"]
      pass

      """  output parameters  """  

