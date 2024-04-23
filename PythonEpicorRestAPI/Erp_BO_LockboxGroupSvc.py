import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LockboxGroupSvc
# Description: Lockbox Group BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LockboxGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LockboxGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LockboxGroups
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups",headers=creds) as resp:
           return await resp.json()

async def post_LockboxGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LockboxGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LockboxGroups_Company_GroupID(Company, GroupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LockboxGroup item
   Description: Calls GetByID to retrieve the LockboxGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LockboxGroups_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LockboxGroup for the service
   Description: Calls UpdateExt to update LockboxGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LockboxGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LockboxGroups_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LockboxGroup item
   Description: Call UpdateExt to delete LockboxGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LockboxGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LockboxGroups_Company_GroupID_Lockboxes(Company, GroupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Lockboxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Lockboxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups(" + Company + "," + GroupID + ")/Lockboxes",headers=creds) as resp:
           return await resp.json()

async def get_LockboxGroups_Company_GroupID_Lockboxes_Company_GroupID_LockboxID(Company, GroupID, LockboxID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Lockbox item
   Description: Calls GetByID to retrieve the Lockbox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Lockbox1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param LockboxID: Desc: LockboxID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/LockboxGroups(" + Company + "," + GroupID + ")/Lockboxes(" + Company + "," + GroupID + "," + LockboxID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Lockboxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Lockboxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Lockboxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/Lockboxes",headers=creds) as resp:
           return await resp.json()

async def post_Lockboxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Lockboxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/Lockboxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Lockboxes_Company_GroupID_LockboxID(Company, GroupID, LockboxID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Lockbox item
   Description: Calls GetByID to retrieve the Lockbox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Lockbox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param LockboxID: Desc: LockboxID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/Lockboxes(" + Company + "," + GroupID + "," + LockboxID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Lockboxes_Company_GroupID_LockboxID(Company, GroupID, LockboxID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Lockbox for the service
   Description: Calls UpdateExt to update Lockbox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Lockbox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param LockboxID: Desc: LockboxID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/Lockboxes(" + Company + "," + GroupID + "," + LockboxID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Lockboxes_Company_GroupID_LockboxID(Company, GroupID, LockboxID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Lockbox item
   Description: Call UpdateExt to delete Lockbox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Lockbox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param LockboxID: Desc: LockboxID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/Lockboxes(" + Company + "," + GroupID + "," + LockboxID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxGroupListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLockboxGroup, whereClauseLockbox, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseLockboxGroup=" + whereClauseLockboxGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLockbox=" + whereClauseLockbox
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LoadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadFile
   Description: This method will read the file and create the LockBoxBatchHead and LockBoxBatchDtl records.
   OperationID: LoadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnBankAcctChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnBankAcctChange
   Description: This method is called when the Bank Account changes
   OperationID: OnBankAcctChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnBankAcctChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnBankAcctChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPayMethodChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPayMethodChange
   Description: This method is called when the Payment Method changes
   OperationID: OnPayMethodChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPayMethodChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPayMethodChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnLockboxDateChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnLockboxDateChange
   Description: This method is called when the Lockbox Group Date changes
   OperationID: OnLockboxDateChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnLockboxDateChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnLockboxDateChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnLockboxLayoutChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnLockboxLayoutChange
   Description: This method is called when the Lockbox Layout ID changes
   OperationID: OnLockboxLayoutChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnLockboxLayoutChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnLockboxLayoutChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePreviewDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePreviewDS
   Description: This method will generate a DataSet to be used when previewing the file contents
   OperationID: GeneratePreviewDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePreviewDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePreviewDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePreviewDSForRecordType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePreviewDSForRecordType
   Description: This method will generate a DataSet to be used when previewing the file contents
   OperationID: GeneratePreviewDSForRecordType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePreviewDSForRecordType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePreviewDSForRecordType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePreviewDSRecordType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePreviewDSRecordType
   Description: This method will generate a DataSet to be used when previewing the file contents
   OperationID: GeneratePreviewDSRecordType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePreviewDSRecordType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePreviewDSRecordType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLockboxGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLockboxGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockboxGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockboxGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockboxGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLockbox(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLockbox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockbox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockbox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockbox_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxGroupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxGroupListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxGroupListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxRow] = obj["value"]
      pass

class Erp_Tablesets_LockboxGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  The GroupID is assigned by the user.  The GroupID establishes the lockbox date and fiscal period defaults for lockboxes assigned to the Group.  """  
      self.LockboxDate:str = obj["LockboxDate"]
      """  Date for all lockboxes within this batch.  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding Lockbox Date using the company's fiscal calendar.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Period which provides one of the defaults to be used when creating lockboxes within this group.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group.  """  
      self.PostingInProcess:bool = obj["PostingInProcess"]
      """  PostingInProcess  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The bank account assigned by the user for the Cash receipt group.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment method will be assigned to all the transactions included on the Lockbox ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  The GroupID is assigned by the user.  The GroupID establishes the lockbox date and fiscal period defaults for lockboxes assigned to the Group.  """  
      self.LockboxDate:str = obj["LockboxDate"]
      """  Date for all lockboxes within this batch.  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding Lockbox Date using the company's fiscal calendar.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Period which provides one of the defaults to be used when creating lockboxes within this group.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group.  """  
      self.PostingInProcess:bool = obj["PostingInProcess"]
      """  PostingInProcess  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The bank account assigned by the user for the Cash receipt group.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment method will be assigned to all the transactions included on the Lockbox ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      """  This field will be used to filter the bank accounts allowed, only those in base currency can be used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Reference to the group  """  
      self.LockboxID:str = obj["LockboxID"]
      """  Reference to Lockbox value  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BankFilePath:str = obj["BankFilePath"]
      """  Location of the bank file identified by the LockboxID.  """  
      self.ProcessedDate:str = obj["ProcessedDate"]
      """  Date when processed  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Indicates if the file has been loaded and is ready to process.  """  
      self.TransmissionDate:str = obj["TransmissionDate"]
      """  Transmission Date from loaded file.  """  
      self.TransmissionTime:int = obj["TransmissionTime"]
      """  Transmission Time from loaded file.  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  Error Message  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User who created it  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Creation date  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.HasError:bool = obj["HasError"]
      """  Used in the lockbox grid so the user can quickly see which records have errors.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LockboxGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  The GroupID is assigned by the user.  The GroupID establishes the lockbox date and fiscal period defaults for lockboxes assigned to the Group.  """  
      self.LockboxDate:str = obj["LockboxDate"]
      """  Date for all lockboxes within this batch.  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding Lockbox Date using the company's fiscal calendar.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Period which provides one of the defaults to be used when creating lockboxes within this group.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group.  """  
      self.PostingInProcess:bool = obj["PostingInProcess"]
      """  PostingInProcess  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The bank account assigned by the user for the Cash receipt group.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment method will be assigned to all the transactions included on the Lockbox ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxGroupListTableset:
   def __init__(self, obj):
      self.LockboxGroupList:list[Erp_Tablesets_LockboxGroupListRow] = obj["LockboxGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LockboxGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  The GroupID is assigned by the user.  The GroupID establishes the lockbox date and fiscal period defaults for lockboxes assigned to the Group.  """  
      self.LockboxDate:str = obj["LockboxDate"]
      """  Date for all lockboxes within this batch.  """  
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding Lockbox Date using the company's fiscal calendar.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Period which provides one of the defaults to be used when creating lockboxes within this group.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group.  """  
      self.PostingInProcess:bool = obj["PostingInProcess"]
      """  PostingInProcess  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  The bank account assigned by the user for the Cash receipt group.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment method will be assigned to all the transactions included on the Lockbox ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      """  This field will be used to filter the bank accounts allowed, only those in base currency can be used.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxGroupTableset:
   def __init__(self, obj):
      self.LockboxGroup:list[Erp_Tablesets_LockboxGroupRow] = obj["LockboxGroup"]
      self.Lockbox:list[Erp_Tablesets_LockboxRow] = obj["Lockbox"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LockboxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.GroupID:str = obj["GroupID"]
      """  Reference to the group  """  
      self.LockboxID:str = obj["LockboxID"]
      """  Reference to Lockbox value  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BankFilePath:str = obj["BankFilePath"]
      """  Location of the bank file identified by the LockboxID.  """  
      self.ProcessedDate:str = obj["ProcessedDate"]
      """  Date when processed  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  Indicates if the file has been loaded and is ready to process.  """  
      self.TransmissionDate:str = obj["TransmissionDate"]
      """  Transmission Date from loaded file.  """  
      self.TransmissionTime:int = obj["TransmissionTime"]
      """  Transmission Time from loaded file.  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  Error Message  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User who created it  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Creation date  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.HasError:bool = obj["HasError"]
      """  Used in the lockbox grid so the user can quickly see which records have errors.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtLockboxGroupTableset:
   def __init__(self, obj):
      self.LockboxGroup:list[Erp_Tablesets_LockboxGroupRow] = obj["LockboxGroup"]
      self.Lockbox:list[Erp_Tablesets_LockboxRow] = obj["Lockbox"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GeneratePreviewDSForRecordType_input:
   """ Required : 
   LayoutID
   recordTypeID
   filepath
   """  
   def __init__(self, obj):
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID used by the Group  """  
      self.recordTypeID:str = obj["recordTypeID"]
      """  Record type to preview  """  
      self.filepath:str = obj["filepath"]
      """  Path of the server lockbox file  """  
      pass

class GeneratePreviewDSForRecordType_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GeneratePreviewDSRecordType_input:
   """ Required : 
   LayoutID
   recordTypeID
   filepath
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID used by the Group  """  
      self.recordTypeID:str = obj["recordTypeID"]
      """  Record type to preview  """  
      self.filepath:str = obj["filepath"]
      """  Path of the server lockbox file  """  
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GeneratePreviewDSRecordType_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GeneratePreviewDS_input:
   """ Required : 
   LayoutID
   filepath
   """  
   def __init__(self, obj):
      self.LayoutID:str = obj["LayoutID"]
      """  LayoutID used by the Group  """  
      self.filepath:str = obj["filepath"]
      """  Path of the server lockbox file  """  
      pass

class GeneratePreviewDS_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LockboxGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxGroupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxGroupListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLockboxGroup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class GetNewLockboxGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLockbox_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewLockbox_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLockboxGroup
   whereClauseLockbox
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLockboxGroup:str = obj["whereClauseLockboxGroup"]
      self.whereClauseLockbox:str = obj["whereClauseLockbox"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LockboxGroupTableset] = obj["returnObj"]
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

class LoadFile_input:
   """ Required : 
   GroupID
   LockboxID
   filepath
   """  
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  GroupID for the Lockbox  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID for the Lockbox  """  
      self.filepath:str = obj["filepath"]
      """  Server path of the lockbox file  """  
      pass

class LoadFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnBankAcctChange_input:
   """ Required : 
   BankAcctId
   ds
   """  
   def __init__(self, obj):
      self.BankAcctId:str = obj["BankAcctId"]
      """  Proposed Bank Account  """  
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class OnBankAcctChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnLockboxDateChange_input:
   """ Required : 
   LockboxDate
   ds
   """  
   def __init__(self, obj):
      self.LockboxDate:str = obj["LockboxDate"]
      """  Proposed Lockbox Group Date  """  
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class OnLockboxDateChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnLockboxLayoutChange_input:
   """ Required : 
   LayoutID
   ds
   """  
   def __init__(self, obj):
      self.LayoutID:str = obj["LayoutID"]
      """  Proposed LayoutId  """  
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class OnLockboxLayoutChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnPayMethodChange_input:
   """ Required : 
   PMUID
   ds
   """  
   def __init__(self, obj):
      self.PMUID:int = obj["PMUID"]
      """  Proposed Payment Method  """  
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class OnPayMethodChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLockboxGroupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLockboxGroupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxGroupTableset] = obj["ds"]
      pass

      """  output parameters  """  

