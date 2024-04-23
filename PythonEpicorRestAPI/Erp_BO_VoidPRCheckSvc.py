import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VoidPRCheckSvc
# Description: VoidPRCheckSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VoidPRChecks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VoidPRChecks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VoidPRChecks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks",headers=creds) as resp:
           return await resp.json()

async def post_VoidPRChecks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VoidPRChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VoidPRChecks_Company_HeadNum(Company, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VoidPRCheck item
   Description: Calls GetByID to retrieve the VoidPRCheck item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VoidPRCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VoidPRChecks_Company_HeadNum(Company, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VoidPRCheck for the service
   Description: Calls UpdateExt to update VoidPRCheck. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VoidPRCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRCheckRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VoidPRChecks_Company_HeadNum(Company, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VoidPRCheck item
   Description: Call UpdateExt to delete VoidPRCheck item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VoidPRCheck
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/VoidPRChecks(" + Company + "," + HeadNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRCheckListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRCheck, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePRCheck=" + whereClausePRCheck
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_getClientFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getClientFileName
   OperationID: getClientFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEmpID
   Description: Call this method from Kinetic before calling OnChangeEmployeeID as that method acts more like the GetByID and
we need to validate if the EmpID is valid first.
   OperationID: ValidateEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEmployeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEmployeeID
   Description: Call this method after user enters the Employee ID.
   OperationID: OnChangeEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreVoidCheck(epicorHeaders = None):
   """  
   Summary: Invoke method PreVoidCheck
   Description: check if interface
   OperationID: PreVoidCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreVoidCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_VoidPayrollCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidPayrollCheck
   OperationID: VoidPayrollCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPayrollCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPayrollCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRCheck
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPRCheckSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRCheckListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRCheckRow] = obj["value"]
      pass

class Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.EmpID:str = obj["EmpID"]
      self.AddressList:str = obj["AddressList"]
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.PhotoFile:str = obj["PhotoFile"]
      self.ImageFile:str = obj["ImageFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      """  Description of the workers' compensation code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActiveToPrint:bool = obj["ActiveToPrint"]
      """  ActiveToPrint  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.ImageFile:str = obj["ImageFile"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.AddressList:str = obj["AddressList"]
      self.AddressListFormatted:str = obj["AddressListFormatted"]
      """  The columns is the formatted by new line separator version of the AddressList column  """  
      self.DspCheckAmt:int = obj["DspCheckAmt"]
      """  Display CheckAmt for kinetic  """  
      self.DspCheckDate:str = obj["DspCheckDate"]
      """  Display CheckDate for kinetic  """  
      self.DspCheckNum:int = obj["DspCheckNum"]
      """  Display CheckNum for kinetic  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PRCheckListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.EmpID:str = obj["EmpID"]
      self.AddressList:str = obj["AddressList"]
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.PhotoFile:str = obj["PhotoFile"]
      self.ImageFile:str = obj["ImageFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      """  Full description of the payroll class.  """  
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      """  Description of the workers' compensation code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRCheckListTableset:
   def __init__(self, obj):
      self.PRCheckList:list[Erp_Tablesets_PRCheckListRow] = obj["PRCheckList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRCheckRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" that the check belongs to.  All checks belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "PRCheckSeq".  HeadNum + Company creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.EmpLink:str = obj["EmpLink"]
      """  Encoded value which identifies the employee.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.PSDate:str = obj["PSDate"]
      """  Pay period start date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.PEDate:str = obj["PEDate"]
      """  Pay period end date for this check.  This is updated as part of the payroll posting process for system generated checks.  It is entered by the user for manual checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to.  Updated during the check printing process for system printed checks or updated based on the CheckDate for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G/L fiscal period that this check is posted to.  Updated by the check printing process for system printed checks.  For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.TotalBasePay:int = obj["TotalBasePay"]
      """  Total Base Pay for this check. Not user maintainable.  It summarizes all PRChkDtl for the check.  Updated via PRChkDtl write/delete triggers. The triggers update this with  (BasePay + PremiumPay + PremiumBasePay + ShiftPay)  """  
      self.TotalPremiumPay:int = obj["TotalPremiumPay"]
      """  Total Premium Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.PremiumPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalShiftPay:int = obj["TotalShiftPay"]
      """  Total Shift Pay for this check.  Not user maintainable.  It summarizes all PRChkDtl.ShiftPay for the check.  Updated via PRChkDtl write/delete triggers.  """  
      self.TotalTaxes:int = obj["TotalTaxes"]
      """  Total of all Tax amounts for the check.  Not user maintainable.  It summarizes all PRChkTax.TaxAmt for the check.  Updated via PRChkTax write/delete triggers.  """  
      self.TotalDeductions:int = obj["TotalDeductions"]
      """  Total of all deduction amounts for the check.  Not user maintainable.  It summarizes all PRChkDed.DeductionAmt for the check.  Updated via PRChkDed write/delete triggers.  """  
      self.TotalBaseHours:int = obj["TotalBaseHours"]
      """  Total Base Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.BaseHours updated via the PRChkDtl write/delete triggers  """  
      self.TotalPremiumHours:int = obj["TotalPremiumHours"]
      """  Total Premium Hours on this check. Not directly maintainable by user. A summary of PRChkDtl.PremiumHours updated via the PRChkDtl write/delete triggers  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Net Check Amount.  Not directly user maintainable.  Updated as (PRCheck.TotalBasePay + TotalPremiumPay + ShiftPay + NonTaxAmt) - (TotalTaxes + TotalDeductions).  Updated via write trigger on PRCheck.  """  
      self.StartupCheck:bool = obj["StartupCheck"]
      """  Indicates that the check was created using the YTD Startup routines.  This is not a real check.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.WorkCompCode:str = obj["WorkCompCode"]
      """  The WorkCompCode relates this check to the proper WorkComp master.  Used in the Worker's Comp report.  It is duplicated from the PREmpMas.WorkCompCode during the posting process.  """  
      self.ClassID:str = obj["ClassID"]
      """  Payroll class ID that employee is currently assigned to. A mirror image of PREmpMas. It is kept in sync by the PREmpMas write trigger.  """  
      self.Note:str = obj["Note"]
      """  A short note which is printed on the check.  """  
      self.PayFrequency:str = obj["PayFrequency"]
      """  Copied from PREmpMas at the time the PRCheck record is created.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bankslip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ActiveToPrint:bool = obj["ActiveToPrint"]
      """  ActiveToPrint  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.VoidedDate:str = obj["VoidedDate"]
      """  VoidedDate  """  
      self.EmpFirstName:str = obj["EmpFirstName"]
      self.EmpID:str = obj["EmpID"]
      self.EmpLastName:str = obj["EmpLastName"]
      self.EmpLinkFirstName:str = obj["EmpLinkFirstName"]
      self.EmpLinkLastName:str = obj["EmpLinkLastName"]
      self.EmpLinkName:str = obj["EmpLinkName"]
      self.EmpMiddleInit:str = obj["EmpMiddleInit"]
      self.ImageFile:str = obj["ImageFile"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      self.PRInterfacedContinue:bool = obj["PRInterfacedContinue"]
      """  Used in VoidPRCheck - User response to a question when GL is not interfaced.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SocSecNum:str = obj["SocSecNum"]
      self.AddressList:str = obj["AddressList"]
      self.AddressListFormatted:str = obj["AddressListFormatted"]
      """  The columns is the formatted by new line separator version of the AddressList column  """  
      self.DspCheckAmt:int = obj["DspCheckAmt"]
      """  Display CheckAmt for kinetic  """  
      self.DspCheckDate:str = obj["DspCheckDate"]
      """  Display CheckDate for kinetic  """  
      self.DspCheckNum:int = obj["DspCheckNum"]
      """  Display CheckNum for kinetic  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.ClassIDDescription:str = obj["ClassIDDescription"]
      self.WorkCompCodeDescription:str = obj["WorkCompCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtVoidPRCheckTableset:
   def __init__(self, obj):
      self.PRCheck:list[Erp_Tablesets_PRCheckRow] = obj["PRCheck"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VoidPRCheckPREmpMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DisplayAddress:str = obj["DisplayAddress"]
      """  Name and address combined in one field.  """  
      self.SupervisorName:str = obj["SupervisorName"]
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.EmpID:str = obj["EmpID"]
      self.PRInterfaced:bool = obj["PRInterfaced"]
      self.ImageFile:str = obj["ImageFile"]
      """  Path of photo id  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VoidPRCheckPREmpMasTableset:
   def __init__(self, obj):
      self.VoidPRCheckPREmpMas:list[Erp_Tablesets_VoidPRCheckPREmpMasRow] = obj["VoidPRCheckPREmpMas"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VoidPRCheckTableset:
   def __init__(self, obj):
      self.PRCheck:list[Erp_Tablesets_PRCheckRow] = obj["PRCheck"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VoidPRCheckTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VoidPRCheckTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VoidPRCheckTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PRCheckListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPRCheck_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckTableset] = obj["ds"]
      pass

class GetNewPRCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRCheck
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRCheck:str = obj["whereClausePRCheck"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VoidPRCheckTableset] = obj["returnObj"]
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

class OnChangeEmployeeID_input:
   """ Required : 
   ds
   pcEmployeeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckPREmpMasTableset] = obj["ds"]
      self.pcEmployeeID:str = obj["pcEmployeeID"]
      """  Employee ID  """  
      pass

class OnChangeEmployeeID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VoidPRCheckTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckPREmpMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreVoidCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.InterfacedText:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVoidPRCheckTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVoidPRCheckTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPRCheckTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateEmpID_input:
   """ Required : 
   pcEmployeeID
   """  
   def __init__(self, obj):
      self.pcEmployeeID:str = obj["pcEmployeeID"]
      """  Employee ID  """  
      pass

class ValidateEmpID_output:
   def __init__(self, obj):
      pass

class VoidPayrollCheck_input:
   """ Required : 
   ipCheckNum
   ipVoidDate
   ipEmployeeId
   ipPRInterfacedContinue
   """  
   def __init__(self, obj):
      self.ipCheckNum:int = obj["ipCheckNum"]
      self.ipVoidDate:str = obj["ipVoidDate"]
      self.ipEmployeeId:str = obj["ipEmployeeId"]
      self.ipPRInterfacedContinue:bool = obj["ipPRInterfacedContinue"]
      pass

class VoidPayrollCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oErrMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class getClientFileName_input:
   """ Required : 
   IP_ServerFileName
   """  
   def __init__(self, obj):
      self.IP_ServerFileName:str = obj["IP_ServerFileName"]
      pass

class getClientFileName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

