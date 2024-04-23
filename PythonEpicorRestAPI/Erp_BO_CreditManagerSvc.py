import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CreditManagerSvc
# Description: Customer Credit Manager Business Object
           Notes : The logic for the update of the Customer Credit Information is copied
           from the Customer Business Object.  Limit the fields to be maintained
           for Customer since validation is limited to just the update of credit
           information.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditManagers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditManagers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CMCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers",headers=creds) as resp:
           return await resp.json()

async def post_CreditManagers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditManagers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers_Company_CustNum(Company, CustNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditManager item
   Description: Calls GetByID to retrieve the CreditManager item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditManager
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditManagers_Company_CustNum(Company, CustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditManager for the service
   Description: Calls UpdateExt to update CreditManager. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditManager
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditManagers_Company_CustNum(Company, CustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditManager item
   Description: Call UpdateExt to delete CreditManager item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditManager
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers_Company_CustNum_CustomCrdPools(Company, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CustomCrdPools items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustomCrdPools1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomCrdPoolRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/CustomCrdPools",headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers_Company_CustNum_CustomCrdPools_SysRowID(Company, CustNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustomCrdPool item
   Description: Calls GetByID to retrieve the CustomCrdPool item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomCrdPool1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/CustomCrdPools(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers_Company_CustNum_GlbCustCreds(Company, CustNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GlbCustCreds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCustCreds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustCredRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/GlbCustCreds",headers=creds) as resp:
           return await resp.json()

async def get_CreditManagers_Company_CustNum_GlbCustCreds_Company_CustNum_ExtCompany(Company, CustNum, ExtCompany, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCustCred item
   Description: Calls GetByID to retrieve the GlbCustCred item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustCred1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ExtCompany: Desc: ExtCompany   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustomCrdPools(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustomCrdPools items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustomCrdPools
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomCrdPoolRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools",headers=creds) as resp:
           return await resp.json()

async def post_CustomCrdPools(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustomCrdPools
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustomCrdPools_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustomCrdPool item
   Description: Calls GetByID to retrieve the CustomCrdPool item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomCrdPool
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustomCrdPools_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustomCrdPool for the service
   Description: Calls UpdateExt to update CustomCrdPool. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustomCrdPool
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustomCrdPools_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustomCrdPool item
   Description: Call UpdateExt to delete CustomCrdPool item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustomCrdPool
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCustCreds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCustCreds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCustCreds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustCredRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds",headers=creds) as resp:
           return await resp.json()

async def post_GlbCustCreds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCustCreds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCustCreds_Company_CustNum_ExtCompany(Company, CustNum, ExtCompany, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCustCred item
   Description: Calls GetByID to retrieve the GlbCustCred item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustCred
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ExtCompany: Desc: ExtCompany   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCustCreds_Company_CustNum_ExtCompany(Company, CustNum, ExtCompany, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCustCred for the service
   Description: Calls UpdateExt to update GlbCustCred. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCustCred
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ExtCompany: Desc: ExtCompany   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCustCreds_Company_CustNum_ExtCompany(Company, CustNum, ExtCompany, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCustCred item
   Description: Call UpdateExt to delete GlbCustCred item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCustCred
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ExtCompany: Desc: ExtCompany   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CMCustomerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCMCustomer, whereClauseCustomCrdPool, whereClauseGlbCustCred, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseCMCustomer=" + whereClauseCMCustomer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustomCrdPool=" + whereClauseCustomCrdPool
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlbCustCred=" + whereClauseGlbCustCred
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, epicorHeaders = None):
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
   params += "custNum=" + custNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_isNAGlobalCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method isNAGlobalCustomer
   OperationID: isNAGlobalCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isNAGlobalCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isNAGlobalCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomerGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomerGlobalFields
   OperationID: GetCustomerGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCollections(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCollections
   Description: Purpose:
Parameters:
<param name="ipInCollections">switch identifying whether or not the customer is in collections</param><param name="ds">The CreditManager data set</param>
Notes:
   OperationID: ChangeCollections
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCollections_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderCreditHold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderCreditHold
   Description: Call this method when the user updates the order's credit hold field.  This will calculate
or reset the default Credit Override Limit of a particular order.  The toggling of the
credit hold check box will determine when OrderHed.CreditOverrideLimit should be enabled.
The Credit Override Limit should be enabled if the Credit Hold field is unchecked.
Conversely, Credit Override Limit is disabled if Credit Hold is checked.
   OperationID: ChangeOrderCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoiceCreditHold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoiceCreditHold
   Description: Validates the Credit Hold change. If valid updates it in the DB.
   OperationID: ChangeInvoiceCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInvoiceCreditHoldByInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInvoiceCreditHoldByInvoiceNum
   Description: Validates the change of Credit Hold in selected InvoiceNum. If Credit hold is valid, it gets updated in the DB.
   OperationID: ChangeInvoiceCreditHoldByInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceCreditHoldByInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceCreditHoldByInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCreditHold(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCreditHold
   Description: This method checks if customer will go on credit hold.  Then asks if the user
wants all orders to go on credit hold.  To be called right before update.  If the user
answers yes to putting orders on hold then the ApplyHoldToOrder field needs to be populated.
   OperationID: CheckCreditHold
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportCustCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportCustCredit
   Description: Call this method to export customer credit information.  This method accepts
an input parameter to exclude or include customer with credit limit of zero.
This method returns the data table ttExportCustCred containing all valid
customer credit information.  The resulting records from the ttExportCustCred
will then need to be outputted as a CSV file (comma delimited) with the first
output line containing the description or label of all fields.
   OperationID: ExportCustCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportCustCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCustCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportCustCreditFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportCustCreditFile
   Description: Call this method to export customer credit information.  This method accepts
an input parameter to exclude or include customer with credit limit of zero.
This method returns the data table ttExportCustCred containing all valid
customer credit information and create a CSV file (comma delimited).
   OperationID: ExportCustCreditFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportCustCreditFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCustCreditFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARLOC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARLOC
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The ARLOCDataSet data set</returns>
   OperationID: GetARLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByCustID
   Description: This method finds the customer record by CustId instead of CustNum
   OperationID: GetByCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDeposits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDeposits
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetCashDeposits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContacts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContacts
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The CustCntDataSet data set</returns>
   OperationID: GetContacts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContacts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContacts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvoicedDeposits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvoicedDeposits
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><param name="ds1"></param>
   OperationID: GetInvoicedDeposits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoicedDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoicedDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvoices
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvoicesEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvoicesEx
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="mode">Valid options are All, Open, Closed, OpenWithDep (GetInvoices original behavior)</param><param name="fromDays">the amount of days to get a date from which the invoices will be selected.</param><param name="inRange">if the invoices will be selected from an specific date.</param><param name="ds"></param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetInvoicesEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoicesEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoicesEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOrders
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The CMOrderHedDataSet data set</returns>
   OperationID: GetOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPayIns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPayIns
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The ARPNHeadDataSet data set</returns>
   OperationID: GetPayIns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayIns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayIns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPayments
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><returns>The CashHeadDataSet data set</returns>
   OperationID: GetPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPaymentsHeaders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPaymentsHeaders
   Description: Get list of Payments (CashHead) for the selected customer.
   OperationID: GetPaymentsHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPaymentsHeaders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentsHeaders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPaymentsDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPaymentsDetails
   Description: Receives GroupID and HeadNum and returns all CashDetails related to this filters.
   OperationID: GetPaymentsDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPaymentsDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentsDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomerBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomerBalance
   Description: Purpose: Retrieves the total unallocated amount of a customer
Parameters:  none
Notes:
<param name="custNum">the customer numeric ID</param><param name="balance">balance in favor of the customer in base currency</param><param name="rpt1Balance">balance in favor of the customer in reporting currency 1</param><param name="rpt2Balance">balance in favor of the customer in reporting currency 2</param><param name="rpt3Balance">balance in favor of the customer in reporting currency 3</param><returns>nothing</returns>
   OperationID: GetCustomerBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomerBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportCustCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportCustCredit
   Description: Call this method to import customer credit information into the database.
This method expects an input data table ttImportCustCred with data coming
from an external comma delimited file.
   OperationID: ImportCustCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCustCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportCustCreditCsv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportCustCreditCsv
   Description: Call this method to import customer credit information into the database.
This method expects the input File to exist in the server with data coming
from an external comma delimited file.
   OperationID: ImportCustCreditCsv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCustCreditCsv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustCreditCsv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCMOrderHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCMOrderHed
   Description: This method updates the ttCMOrderHed's physical table
   OperationID: UpdateCMOrderHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCMOrderHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCMOrderHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateNACreditPrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateNACreditPrc
   Description: This method reset NACreditPrc when its status changes, based in its Used/Shared.
   OperationID: UpdateNACreditPrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNACreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNACreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCreditTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCreditTotals
   Description: This method updates the TotOpenCredit and TotGlobalCredit fields.  To be called when
the include credit flags are changed.
   OperationID: UpdateCreditTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCreditTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCreditTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateGlobalLimits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateGlobalLimits
   Description: This method converts the global credit limit from the global currency value to
the local currency value.  To be used when the global currency code changes or
when the global credit limits are changed.
   OperationID: UpdateGlobalLimits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateGlobalLimits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateGlobalLimits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNAParentCreditPrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNAParentCreditPrc
   Description: This method validates the NA parent credit percentage.
   OperationID: ValidateNAParentCreditPrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNAParentCreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNAParentCreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNACreditSharedPrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNACreditSharedPrc
   Description: This method validate the NA credit shared percentage.
   OperationID: ValidateNACreditSharedPrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNACreditSharedPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNACreditSharedPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGlbNAParentCreditPrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGlbNAParentCreditPrc
   Description: This method validates the global NA parent credit percentage.
   OperationID: ValidateGlbNAParentCreditPrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGlbNAParentCreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGlbNAParentCreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateGlbNACreditSharedPrc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGlbNACreditSharedPrc
   Description: This method validate the global NA credit shared percentage.
   OperationID: ValidateGlbNACreditSharedPrc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGlbNACreditSharedPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGlbNACreditSharedPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAgingCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAgingCode
   Description: Validates Aging Code.
   OperationID: ValidateAgingCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAgingCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAgingCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetOrdersCreditOverride(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetOrdersCreditOverride
   OperationID: SetOrdersCreditOverride
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetOrdersCreditOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrdersCreditOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PESelectInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PESelectInvoices
   Description: This procedure returns Open balance invoices
   OperationID: PESelectInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PESelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PESelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PEUpdateInvcHeadRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PEUpdateInvcHeadRecords
   Description: This procedure updates selected InvcHead
   OperationID: PEUpdateInvcHeadRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PEUpdateInvcHeadRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEUpdateInvcHeadRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCMCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCMCustomer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCMCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCMCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCMCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCustCred(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCustCred
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCustCred
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCustCred_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCustCred_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CMCustomerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CMCustomerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustomCrdPoolRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCustCredRow] = obj["value"]
      pass

class Erp_Tablesets_CMCustomerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      """  allow use Parent Credit in National Account  """  
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the National account  """  
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      """  define what type of credit will be used first when the customer  """  
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      """  Max Percent of Parent Credit to Use  """  
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Children.  """  
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      """  allow use Global Parent Credit in National Account  """  
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the Global National account  """  
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      """  Max Percent of Global Parent Credit to Use  """  
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Global Children.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotOpenInvoices:int = obj["TotOpenInvoices"]
      """  Total number of open invoices  """  
      self.TotOpenOrders:int = obj["TotOpenOrders"]
      """  Total number of open orders  """  
      self.TotOpenPI:int = obj["TotOpenPI"]
      """  Total number of open Payment Instruments  """  
      self.TotInvoiceCredit:int = obj["TotInvoiceCredit"]
      self.TotOrderCredit:int = obj["TotOrderCredit"]
      self.TotPICredit:int = obj["TotPICredit"]
      self.TotOpenCredit:int = obj["TotOpenCredit"]
      """  Total Credit based on CredInc flags  """  
      self.TotGlbInvoiceCredit:int = obj["TotGlbInvoiceCredit"]
      """  Total Global Invoice Credit (including current company)  """  
      self.TotGlbOrderCredit:int = obj["TotGlbOrderCredit"]
      """  Total Global Order Credit (including current company)  """  
      self.TotGlbPICredit:int = obj["TotGlbPICredit"]
      """  Total Global Payment Instruments Credit (including current company)  """  
      self.TotGlbOpenCredit:int = obj["TotGlbOpenCredit"]
      """  Total Global Open Credit (based on GlbCredInc flags)  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Customer is Global (master or linked)  """  
      self.PIFlag:bool = obj["PIFlag"]
      """  Indicates whether PI fields should be enabled or not  """  
      self.ApplyHoldToOrders:bool = obj["ApplyHoldToOrders"]
      """  Apply credit hold status to orders  """  
      self.FxdTotOrders:int = obj["FxdTotOrders"]
      self.FxdTotPI:int = obj["FxdTotPI"]
      self.FxdOrderCredit:int = obj["FxdOrderCredit"]
      self.FxdPICredit:int = obj["FxdPICredit"]
      self.FxdGlbOrdCredit:int = obj["FxdGlbOrdCredit"]
      self.FxdGlbPICredit:int = obj["FxdGlbPICredit"]
      self.DspGlobalCredIncOrd:bool = obj["DspGlobalCredIncOrd"]
      """  Same value as GlobalCredIncOrd except if customer not global, value is no.  """  
      self.EDITest:bool = obj["EDITest"]
      self.EDITranslator:str = obj["EDITranslator"]
      self.NAOwnCreditAvail:int = obj["NAOwnCreditAvail"]
      """  Own Credit Available  """  
      self.NAOwnCreditUsedDsp:int = obj["NAOwnCreditUsedDsp"]
      self.NAParentCrdAvail:int = obj["NAParentCrdAvail"]
      """  Available Parent?s Credit in National Accout  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      self.NASharedCreditUsedDsp:int = obj["NASharedCreditUsedDsp"]
      self.NAPoolCrdAvail:int = obj["NAPoolCrdAvail"]
      """  Available credit from credit pools to be used by this customer in National account.  """  
      self.NAChildCrdAvail:int = obj["NAChildCrdAvail"]
      """  Customer?s credit available to be shared with his Children in National Account  """  
      self.NAParentsCreditUsedDsp:int = obj["NAParentsCreditUsedDsp"]
      self.GlbNAChildCrdAvail:int = obj["GlbNAChildCrdAvail"]
      """  Global Shared Credit Available  """  
      self.GlbNAOwnCreditUsedDsp:int = obj["GlbNAOwnCreditUsedDsp"]
      self.GlbNAParentCrdAvail:int = obj["GlbNAParentCrdAvail"]
      """  Global Parents Credit Available  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      self.GlbNAParentsCreditUsedDsp:int = obj["GlbNAParentsCreditUsedDsp"]
      self.GlbNAPoolCrdAvail:int = obj["GlbNAPoolCrdAvail"]
      self.GlbNASharedCreditUsedDsp:int = obj["GlbNASharedCreditUsedDsp"]
      self.GlbNAOwnCreditAvail:int = obj["GlbNAOwnCreditAvail"]
      """  Global Own Credit Available  """  
      self.NACreditUpdated:bool = obj["NACreditUpdated"]
      """  National Credit data has been updated and recalculation is needed  """  
      self.NATotalCreditAvail:int = obj["NATotalCreditAvail"]
      """  Total Credit available in the National Account  """  
      self.NATotalCreditUsed:int = obj["NATotalCreditUsed"]
      self.NACreditCust:bool = obj["NACreditCust"]
      """  Is the customer in the National Account of Credit Checking  """  
      self.TotLCCredit:int = obj["TotLCCredit"]
      self.TotLCOpenOrders:int = obj["TotLCOpenOrders"]
      """  Total open order value against LC/ECG  """  
      self.TotLCCumInvoices:int = obj["TotLCCumInvoices"]
      """  Total cumulative invoices against LC/ECG  """  
      self.TotLCInvoiceBal:int = obj["TotLCInvoiceBal"]
      """  Total invoice balance against LC/ECG  """  
      self.TotLCUsed:int = obj["TotLCUsed"]
      """  Total LC/ECG credit used.  """  
      self.TotOpenLC:int = obj["TotOpenLC"]
      """  Total number of open LC/ECG.  """  
      self.TotOpenOrderLC:int = obj["TotOpenOrderLC"]
      """  Total number of open orders against LC/ECG.  """  
      self.TotOpenInvoicesLC:int = obj["TotOpenInvoicesLC"]
      """  Total number of open invoices against LC/ECG.  """  
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CMCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      """  allow use Parent Credit in National Account  """  
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the National account  """  
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      """  define what type of credit will be used first when the customer  """  
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      """  Max Percent of Parent Credit to Use  """  
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Children.  """  
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      """  allow use Global Parent Credit in National Account  """  
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the Global National account  """  
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      """  Max Percent of Global Parent Credit to Use  """  
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Global Children.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Collections:bool = obj["Collections"]
      """  In Collections  """  
      self.CollectionsDate:str = obj["CollectionsDate"]
      """  CollectionsDate  """  
      self.DateCollectionPosted:str = obj["DateCollectionPosted"]
      """  Date Collection Posted  """  
      self.AgingCreditHold:bool = obj["AgingCreditHold"]
      """  Indicates if customer has been placed into an "Aging Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.AgingCreditHoldDate:str = obj["AgingCreditHoldDate"]
      """  Date on which the customer was last placed on aging hold. This field is maintained by the system.  """  
      self.AgingCreditHoldSource:str = obj["AgingCreditHoldSource"]
      """  Indicates how the customer was placed on aging hold.  Valid values are "MANUAL" and "PROCESS".  "MANUAL" means that the user placed the customer on hold.  “PROCESS” means that the Mass Credit Information Update Process places the customer on aging hold.  This field is maintained by the system.  """  
      self.AgingCreditClearUserID:str = obj["AgingCreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's aging hold. This field is maintained by the system.  """  
      self.AgingCreditClearDate:str = obj["AgingCreditClearDate"]
      """  The date that the user last cleared the customer's aging hold. This field is maintained by the system.  """  
      self.AgingCreditCode:str = obj["AgingCreditCode"]
      """  The aging code assigned to the customer.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.TotOpenInvoices:int = obj["TotOpenInvoices"]
      """  Total number of open invoices  """  
      self.TotOpenOrders:int = obj["TotOpenOrders"]
      """  Total number of open orders  """  
      self.TotOpenPI:int = obj["TotOpenPI"]
      """  Total number of open Payment Instruments  """  
      self.TotInvoiceCredit:int = obj["TotInvoiceCredit"]
      self.TotOrderCredit:int = obj["TotOrderCredit"]
      self.TotPICredit:int = obj["TotPICredit"]
      self.TotOpenCredit:int = obj["TotOpenCredit"]
      """  Total Credit based on CredInc flags  """  
      self.TotGlbInvoiceCredit:int = obj["TotGlbInvoiceCredit"]
      """  Total Global Invoice Credit (including current company)  """  
      self.TotGlbOrderCredit:int = obj["TotGlbOrderCredit"]
      """  Total Global Order Credit (including current company)  """  
      self.TotGlbPICredit:int = obj["TotGlbPICredit"]
      """  Total Global Payment Instruments Credit (including current company)  """  
      self.TotGlbOpenCredit:int = obj["TotGlbOpenCredit"]
      """  Total Global Open Credit (based on GlbCredInc flags)  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Customer is Global (master or linked)  """  
      self.PIFlag:bool = obj["PIFlag"]
      """  Indicates whether PI fields should be enabled or not  """  
      self.ApplyHoldToOrders:bool = obj["ApplyHoldToOrders"]
      """  Apply credit hold status to orders  """  
      self.FxdTotOrders:int = obj["FxdTotOrders"]
      self.FxdTotPI:int = obj["FxdTotPI"]
      self.FxdOrderCredit:int = obj["FxdOrderCredit"]
      self.FxdPICredit:int = obj["FxdPICredit"]
      self.FxdGlbOrdCredit:int = obj["FxdGlbOrdCredit"]
      self.FxdGlbPICredit:int = obj["FxdGlbPICredit"]
      self.DspGlobalCredIncOrd:bool = obj["DspGlobalCredIncOrd"]
      """  Same value as GlobalCredIncOrd except if customer not global, value is no.  """  
      self.EDITest:bool = obj["EDITest"]
      self.EDITranslator:str = obj["EDITranslator"]
      self.NAOwnCreditAvail:int = obj["NAOwnCreditAvail"]
      """  Own Credit Available  """  
      self.NAOwnCreditUsedDsp:int = obj["NAOwnCreditUsedDsp"]
      self.NAParentCrdAvail:int = obj["NAParentCrdAvail"]
      """  Available Parent?s Credit in National Accout  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      self.NASharedCreditUsedDsp:int = obj["NASharedCreditUsedDsp"]
      self.NAPoolCrdAvail:int = obj["NAPoolCrdAvail"]
      """  Available credit from credit pools to be used by this customer in National account.  """  
      self.NAChildCrdAvail:int = obj["NAChildCrdAvail"]
      """  Customer?s credit available to be shared with his Children in National Account  """  
      self.NAParentsCreditUsedDsp:int = obj["NAParentsCreditUsedDsp"]
      self.GlbNAChildCrdAvail:int = obj["GlbNAChildCrdAvail"]
      """  Global Shared Credit Available  """  
      self.GlbNAOwnCreditUsedDsp:int = obj["GlbNAOwnCreditUsedDsp"]
      self.GlbNAParentCrdAvail:int = obj["GlbNAParentCrdAvail"]
      """  Global Parents Credit Available  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      self.GlbNAParentsCreditUsedDsp:int = obj["GlbNAParentsCreditUsedDsp"]
      self.GlbNAPoolCrdAvail:int = obj["GlbNAPoolCrdAvail"]
      self.GlbNASharedCreditUsedDsp:int = obj["GlbNASharedCreditUsedDsp"]
      self.GlbNAOwnCreditAvail:int = obj["GlbNAOwnCreditAvail"]
      """  Global Own Credit Available  """  
      self.NACreditUpdated:bool = obj["NACreditUpdated"]
      """  National Credit data has been updated and recalculation is needed  """  
      self.NATotalCreditAvail:int = obj["NATotalCreditAvail"]
      """  Total Credit available in the National Account  """  
      self.NATotalCreditUsed:int = obj["NATotalCreditUsed"]
      self.NACreditCust:bool = obj["NACreditCust"]
      """  Is the customer in the National Account of Credit Checking  """  
      self.TotLCCredit:int = obj["TotLCCredit"]
      self.TotLCOpenOrders:int = obj["TotLCOpenOrders"]
      """  Total open order value against LC/ECG  """  
      self.TotLCCumInvoices:int = obj["TotLCCumInvoices"]
      """  Total cumulative invoices against LC/ECG  """  
      self.TotLCInvoiceBal:int = obj["TotLCInvoiceBal"]
      """  Total invoice balance against LC/ECG  """  
      self.TotLCUsed:int = obj["TotLCUsed"]
      """  Total LC/ECG credit used.  """  
      self.TotOpenLC:int = obj["TotOpenLC"]
      """  Total number of open LC/ECG.  """  
      self.TotOpenOrderLC:int = obj["TotOpenOrderLC"]
      """  Total number of open orders against LC/ECG.  """  
      self.TotOpenInvoicesLC:int = obj["TotOpenInvoicesLC"]
      """  Total number of open invoices against LC/ECG.  """  
      self.CollectionsChanged:bool = obj["CollectionsChanged"]
      """   Indicates ift the Collections was changed by the user but not posted yet.
Used in Peru localization.  """  
      self.CollectionsPostVisible:bool = obj["CollectionsPostVisible"]
      """   Indicates if Post Collections option in Actions menu is supposed to be visible.
Post Collections is used by Peru Localization  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AgingCreditDescription:str = obj["AgingCreditDescription"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomCrdPoolRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CustNum:int = obj["CustNum"]
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      self.CreditUsed:int = obj["CreditUsed"]
      self.CreditAvailable:int = obj["CreditAvailable"]
      self.GlobalNA:bool = obj["GlobalNA"]
      """  Global Pool - shows if the pool belongs to Global National Account  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCustCredRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  Company credit totals came from (not just owner of the global customer)  """  
      self.ExtCompName:str = obj["ExtCompName"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the credit was last updated  """  
      self.DocARTotal:int = obj["DocARTotal"]
      """  Open AR Credit in Global Currency  """  
      self.DocSOTotal:int = obj["DocSOTotal"]
      """  Open Order Credit in Global Currency  """  
      self.DocPITotal:int = obj["DocPITotal"]
      """  Open PI Credit in Global Currency  """  
      self.ARTotal:int = obj["ARTotal"]
      """  AR Credit in local companies base currency  """  
      self.SOTotal:int = obj["SOTotal"]
      """  SO Credit in local companies base currency  """  
      self.PITotal:int = obj["PITotal"]
      """  PI Credit in local companies base currency  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  Holds connection and exchange rate error messages  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  This field holds the associated Global Customer number.  If this is the "parent" customer then it will match the CustNum field.  0 indicates that this is not a global customer at all  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.TotalInvoices:int = obj["TotalInvoices"]
      """  Total Number of Open Invoices  """  
      self.TotalOrders:int = obj["TotalOrders"]
      """  Total Number of Open Orders  """  
      self.TotalPayIns:int = obj["TotalPayIns"]
      """  Total Number of open Payment Instruments  """  
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      """  Parent's Credit used by this customer  """  
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      """  Shared Credit used by children  """  
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      """  Own Credit used by himself  """  
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      """  Global Parent's Credit used by this customer  """  
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      """  Shared Credit used by Global children  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      """  Pool Credit used  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      """  Global Credit Pool used  """  
      self.GlbNAOwnCreditUsed:int = obj["GlbNAOwnCreditUsed"]
      """  Own Credit used by himself  """  
      self.NAExceedLimit:int = obj["NAExceedLimit"]
      """  Allocated Credit exceed Credit Limit  """  
      self.GlbNAExceedLimit:int = obj["GlbNAExceedLimit"]
      """  Allocated Credit exceed Global Credit Limit  """  
      self.ARLOCTotal:int = obj["ARLOCTotal"]
      """  AR Letter of Credit Credit in local companies base currency  """  
      self.DocARLOCTotal:int = obj["DocARLOCTotal"]
      """  Open AR Letter of Credit Credit in Global Currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCollections_input:
   """ Required : 
   ipInCollections
   ds
   """  
   def __init__(self, obj):
      self.ipInCollections:bool = obj["ipInCollections"]
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class ChangeCollections_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoiceCreditHoldByInvoiceNum_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      """  Invoice Number being validated  """  
      self.ds:list[Erp_Tablesets_InvcHeadTableset] = obj["ds"]
      pass

class ChangeInvoiceCreditHoldByInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcHeadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeInvoiceCreditHold_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvcHeadTableset] = obj["ds"]
      pass

class ChangeInvoiceCreditHold_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvcHeadTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderCreditHold_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CMOrderHedTableset] = obj["ds"]
      pass

class ChangeOrderCreditHold_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CMOrderHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCreditHold_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class CheckCreditHold_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARLOCAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LCID:str = obj["LCID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Exchange Rate Lock flag  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.GuarantorName:str = obj["GuarantorName"]
      """  Name of the Letter of Credit Guarantor.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Ship Complete flag  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true, no more commitments to this Letter of Credit.  """  
      self.InactiveReason:str = obj["InactiveReason"]
      """  Reason Letter of Credit was marked Inactive (entered by user).  """  
      self.Closed:bool = obj["Closed"]
      """  If true, Letter of Credit is closed.  """  
      self.FOB:str = obj["FOB"]
      """  Optional.  """  
      self.IssuanceType:str = obj["IssuanceType"]
      """  Free form text.  """  
      self.PackListCopies:str = obj["PackListCopies"]
      """  Free form text.  """  
      self.PlaceOfLoading:str = obj["PlaceOfLoading"]
      """  Free form text.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text comments.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier.  """  
      self.Type:str = obj["Type"]
      """  LC = Letter of Credit, ECG = Export Credit Guarantee  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.InUse:bool = obj["InUse"]
      """  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  """  
      self.OpenLCCredit:int = obj["OpenLCCredit"]
      self.OpenOrderValue:int = obj["OpenOrderValue"]
      self.CumInvoices:int = obj["CumInvoices"]
      self.DocCumInvoices:int = obj["DocCumInvoices"]
      """  Cumulative Invoices  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.DocOpenLCCredit:int = obj["DocOpenLCCredit"]
      """  Open LC Credit  """  
      self.DocOpenOrderValue:int = obj["DocOpenOrderValue"]
      """  Open Order Value  """  
      self.DocPaidInvoiceValue:int = obj["DocPaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.DocTotalOrderValue:int = obj["DocTotalOrderValue"]
      """  Total Order Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.PaidInvoiceValue:int = obj["PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt1CumInvoices:int = obj["Rpt1CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt2CumInvoices:int = obj["Rpt2CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt3CumInvoices:int = obj["Rpt3CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1OpenLCCredit:int = obj["Rpt1OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenLCCredit:int = obj["Rpt2OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt3OpenLCCredit:int = obj["Rpt3OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenOrderValue:int = obj["Rpt2OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1OpenOrderValue:int = obj["Rpt1OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt3OpenOrderValue:int = obj["Rpt3OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1PaidInvoiceValue:int = obj["Rpt1PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt2PaidInvoiceValue:int = obj["Rpt2PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt3PaidInvoiceValue:int = obj["Rpt3PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt1TotalOrderValue:int = obj["Rpt1TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt2TotalOrderValue:int = obj["Rpt2TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt3TotalOrderValue:int = obj["Rpt3TotalOrderValue"]
      """  Total Order Value  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.Currency:str = obj["Currency"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      self.LCValueCurrent:int = obj["LCValueCurrent"]
      """  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  """  
      self.OpenLCCreditCurrent:int = obj["OpenLCCreditCurrent"]
      """  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  """  
      self.OpenOrderValueCurrent:int = obj["OpenOrderValueCurrent"]
      """  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  """  
      self.CumInvoicesCurrent:int = obj["CumInvoicesCurrent"]
      self.InvoiceBalCurrent:int = obj["InvoiceBalCurrent"]
      """  Invoices Balance converted from document cuurency using current (today) exchange rate  """  
      self.PaidInvoiceValueCurrent:int = obj["PaidInvoiceValueCurrent"]
      """  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  """  
      self.TotalOrderValueCurrent:int = obj["TotalOrderValueCurrent"]
      """  Total Order value converted from amount in doc currency using current (now) exchange rate  """  
      self.Rpt1LCValueCurrent:int = obj["Rpt1LCValueCurrent"]
      """  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt2LCValueCurrent:int = obj["Rpt2LCValueCurrent"]
      """  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt3LCValueCurrent:int = obj["Rpt3LCValueCurrent"]
      """  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      self.BTCustNumName:str = obj["BTCustNumName"]
      self.CurrencyCodeBaseCurr:bool = obj["CurrencyCodeBaseCurr"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCTableset:
   def __init__(self, obj):
      self.ARLOC:list[Erp_Tablesets_ARLOCRow] = obj["ARLOC"]
      self.ARLOCAttch:list[Erp_Tablesets_ARLOCAttchRow] = obj["ARLOCAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AllocDepositTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.PrePayType:int = obj["PrePayType"]
      """  "0 - Prepaid Invoiced Deposit   1 - Cash Deposit 2 - Reverse Cash Deposit"  """  
      self.DepInvoiceNum:int = obj["DepInvoiceNum"]
      """  Deposit Invoice Number  """  
      self.DepGroupID:str = obj["DepGroupID"]
      """  Group ID of deposit payment  """  
      self.DepHeadNum:int = obj["DepHeadNum"]
      """  Identification of Deposit Payment  """  
      self.DepApplyDate:str = obj["DepApplyDate"]
      """  Apply Date of Deposit Invoice  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.PrePayStatus:int = obj["PrePayStatus"]
      """  "0 - Unrecognized               1 - Partial Recognized 2 - Full Recognized"  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      """  Allocated Amount  """  
      self.AllocAmt:int = obj["AllocAmt"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.DocAllocBal:int = obj["DocAllocBal"]
      """  Allocated Balance  """  
      self.AllocBal:int = obj["AllocBal"]
      self.Rpt1AllocBal:int = obj["Rpt1AllocBal"]
      self.Rpt2AllocBal:int = obj["Rpt2AllocBal"]
      self.Rpt3AllocBal:int = obj["Rpt3AllocBal"]
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total Tax Amount of Deposit  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.DocAllocTaxBal:int = obj["DocAllocTaxBal"]
      """  Remaining Tax Amount of Deposit  """  
      self.AllocTaxBal:int = obj["AllocTaxBal"]
      self.Rpt1AllocTaxBal:int = obj["Rpt1AllocTaxBal"]
      self.Rpt2AllocTaxBal:int = obj["Rpt2AllocTaxBal"]
      self.Rpt3AllocTaxBal:int = obj["Rpt3AllocTaxBal"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Shipment Invoice Number for which this Deposit is allocated  """  
      self.DepCheckRef:str = obj["DepCheckRef"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.DocOriginalAmt:int = obj["DocOriginalAmt"]
      """  Original Amt  """  
      self.OriginalAmt:int = obj["OriginalAmt"]
      self.Rpt1OriginalAmt:int = obj["Rpt1OriginalAmt"]
      self.Rpt2OriginalAmt:int = obj["Rpt2OriginalAmt"]
      self.Rpt3OriginalAmt:int = obj["Rpt3OriginalAmt"]
      self.DocOriginalTaxAmt:int = obj["DocOriginalTaxAmt"]
      """  Original Tax Amt  """  
      self.OriginalTaxAmt:int = obj["OriginalTaxAmt"]
      self.Rpt1OriginalTaxAmt:int = obj["Rpt1OriginalTaxAmt"]
      self.Rpt2OriginalTaxAmt:int = obj["Rpt2OriginalTaxAmt"]
      self.Rpt3OriginalTaxAmt:int = obj["Rpt3OriginalTaxAmt"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.Reference:str = obj["Reference"]
      self.IsDepCM:bool = obj["IsDepCM"]
      """  IsDepCM to distinguish between Deposit Billing Invoices and Deposit Billing Credit Memos  """  
      self.DepInvoiceDate:str = obj["DepInvoiceDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AllocDepositsTableset:
   def __init__(self, obj):
      self.AllocDepositTrk:list[Erp_Tablesets_AllocDepositTrkRow] = obj["AllocDepositTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CMCustomerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      """  allow use Parent Credit in National Account  """  
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the National account  """  
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      """  define what type of credit will be used first when the customer  """  
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      """  Max Percent of Parent Credit to Use  """  
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Children.  """  
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      """  allow use Global Parent Credit in National Account  """  
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the Global National account  """  
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      """  Max Percent of Global Parent Credit to Use  """  
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Global Children.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotOpenInvoices:int = obj["TotOpenInvoices"]
      """  Total number of open invoices  """  
      self.TotOpenOrders:int = obj["TotOpenOrders"]
      """  Total number of open orders  """  
      self.TotOpenPI:int = obj["TotOpenPI"]
      """  Total number of open Payment Instruments  """  
      self.TotInvoiceCredit:int = obj["TotInvoiceCredit"]
      self.TotOrderCredit:int = obj["TotOrderCredit"]
      self.TotPICredit:int = obj["TotPICredit"]
      self.TotOpenCredit:int = obj["TotOpenCredit"]
      """  Total Credit based on CredInc flags  """  
      self.TotGlbInvoiceCredit:int = obj["TotGlbInvoiceCredit"]
      """  Total Global Invoice Credit (including current company)  """  
      self.TotGlbOrderCredit:int = obj["TotGlbOrderCredit"]
      """  Total Global Order Credit (including current company)  """  
      self.TotGlbPICredit:int = obj["TotGlbPICredit"]
      """  Total Global Payment Instruments Credit (including current company)  """  
      self.TotGlbOpenCredit:int = obj["TotGlbOpenCredit"]
      """  Total Global Open Credit (based on GlbCredInc flags)  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Customer is Global (master or linked)  """  
      self.PIFlag:bool = obj["PIFlag"]
      """  Indicates whether PI fields should be enabled or not  """  
      self.ApplyHoldToOrders:bool = obj["ApplyHoldToOrders"]
      """  Apply credit hold status to orders  """  
      self.FxdTotOrders:int = obj["FxdTotOrders"]
      self.FxdTotPI:int = obj["FxdTotPI"]
      self.FxdOrderCredit:int = obj["FxdOrderCredit"]
      self.FxdPICredit:int = obj["FxdPICredit"]
      self.FxdGlbOrdCredit:int = obj["FxdGlbOrdCredit"]
      self.FxdGlbPICredit:int = obj["FxdGlbPICredit"]
      self.DspGlobalCredIncOrd:bool = obj["DspGlobalCredIncOrd"]
      """  Same value as GlobalCredIncOrd except if customer not global, value is no.  """  
      self.EDITest:bool = obj["EDITest"]
      self.EDITranslator:str = obj["EDITranslator"]
      self.NAOwnCreditAvail:int = obj["NAOwnCreditAvail"]
      """  Own Credit Available  """  
      self.NAOwnCreditUsedDsp:int = obj["NAOwnCreditUsedDsp"]
      self.NAParentCrdAvail:int = obj["NAParentCrdAvail"]
      """  Available Parent?s Credit in National Accout  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      self.NASharedCreditUsedDsp:int = obj["NASharedCreditUsedDsp"]
      self.NAPoolCrdAvail:int = obj["NAPoolCrdAvail"]
      """  Available credit from credit pools to be used by this customer in National account.  """  
      self.NAChildCrdAvail:int = obj["NAChildCrdAvail"]
      """  Customer?s credit available to be shared with his Children in National Account  """  
      self.NAParentsCreditUsedDsp:int = obj["NAParentsCreditUsedDsp"]
      self.GlbNAChildCrdAvail:int = obj["GlbNAChildCrdAvail"]
      """  Global Shared Credit Available  """  
      self.GlbNAOwnCreditUsedDsp:int = obj["GlbNAOwnCreditUsedDsp"]
      self.GlbNAParentCrdAvail:int = obj["GlbNAParentCrdAvail"]
      """  Global Parents Credit Available  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      self.GlbNAParentsCreditUsedDsp:int = obj["GlbNAParentsCreditUsedDsp"]
      self.GlbNAPoolCrdAvail:int = obj["GlbNAPoolCrdAvail"]
      self.GlbNASharedCreditUsedDsp:int = obj["GlbNASharedCreditUsedDsp"]
      self.GlbNAOwnCreditAvail:int = obj["GlbNAOwnCreditAvail"]
      """  Global Own Credit Available  """  
      self.NACreditUpdated:bool = obj["NACreditUpdated"]
      """  National Credit data has been updated and recalculation is needed  """  
      self.NATotalCreditAvail:int = obj["NATotalCreditAvail"]
      """  Total Credit available in the National Account  """  
      self.NATotalCreditUsed:int = obj["NATotalCreditUsed"]
      self.NACreditCust:bool = obj["NACreditCust"]
      """  Is the customer in the National Account of Credit Checking  """  
      self.TotLCCredit:int = obj["TotLCCredit"]
      self.TotLCOpenOrders:int = obj["TotLCOpenOrders"]
      """  Total open order value against LC/ECG  """  
      self.TotLCCumInvoices:int = obj["TotLCCumInvoices"]
      """  Total cumulative invoices against LC/ECG  """  
      self.TotLCInvoiceBal:int = obj["TotLCInvoiceBal"]
      """  Total invoice balance against LC/ECG  """  
      self.TotLCUsed:int = obj["TotLCUsed"]
      """  Total LC/ECG credit used.  """  
      self.TotOpenLC:int = obj["TotOpenLC"]
      """  Total number of open LC/ECG.  """  
      self.TotOpenOrderLC:int = obj["TotOpenOrderLC"]
      """  Total number of open orders against LC/ECG.  """  
      self.TotOpenInvoicesLC:int = obj["TotOpenInvoicesLC"]
      """  Total number of open invoices against LC/ECG.  """  
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CMCustomerListTableset:
   def __init__(self, obj):
      self.CMCustomerList:list[Erp_Tablesets_CMCustomerListRow] = obj["CMCustomerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CMCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date on which the next credit review should be conducted for the customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      """  Date on which the customer was last placed on credit hold. This field is maintained by the system.  """  
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      """  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  """  
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearDate:str = obj["CreditClearDate"]
      """  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  """  
      self.CreditClearTime:str = obj["CreditClearTime"]
      """  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.ICCust:bool = obj["ICCust"]
      """  Determines whether or not this customer is an inter-company customer.  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Determines whether or not this customer is shared between more than one company.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this customer record will receive global updates.  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      """  allow use Parent Credit in National Account  """  
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the National account  """  
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      """  define what type of credit will be used first when the customer  """  
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      """  Max Percent of Parent Credit to Use  """  
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Children.  """  
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      """  allow use Global Parent Credit in National Account  """  
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      """  allow/deny to a customer share his own credit with other customers within the Global National account  """  
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      """  Max Percent of Global Parent Credit to Use  """  
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      """  Percentage of the customer credit shared to his Global Children.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Collections:bool = obj["Collections"]
      """  In Collections  """  
      self.CollectionsDate:str = obj["CollectionsDate"]
      """  CollectionsDate  """  
      self.DateCollectionPosted:str = obj["DateCollectionPosted"]
      """  Date Collection Posted  """  
      self.AgingCreditHold:bool = obj["AgingCreditHold"]
      """  Indicates if customer has been placed into an "Aging Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.AgingCreditHoldDate:str = obj["AgingCreditHoldDate"]
      """  Date on which the customer was last placed on aging hold. This field is maintained by the system.  """  
      self.AgingCreditHoldSource:str = obj["AgingCreditHoldSource"]
      """  Indicates how the customer was placed on aging hold.  Valid values are "MANUAL" and "PROCESS".  "MANUAL" means that the user placed the customer on hold.  “PROCESS” means that the Mass Credit Information Update Process places the customer on aging hold.  This field is maintained by the system.  """  
      self.AgingCreditClearUserID:str = obj["AgingCreditClearUserID"]
      """  The UserFile.DCDUSERID value of the user that last cleared the customer's aging hold. This field is maintained by the system.  """  
      self.AgingCreditClearDate:str = obj["AgingCreditClearDate"]
      """  The date that the user last cleared the customer's aging hold. This field is maintained by the system.  """  
      self.AgingCreditCode:str = obj["AgingCreditCode"]
      """  The aging code assigned to the customer.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the record is inactive.  """  
      self.TotOpenInvoices:int = obj["TotOpenInvoices"]
      """  Total number of open invoices  """  
      self.TotOpenOrders:int = obj["TotOpenOrders"]
      """  Total number of open orders  """  
      self.TotOpenPI:int = obj["TotOpenPI"]
      """  Total number of open Payment Instruments  """  
      self.TotInvoiceCredit:int = obj["TotInvoiceCredit"]
      self.TotOrderCredit:int = obj["TotOrderCredit"]
      self.TotPICredit:int = obj["TotPICredit"]
      self.TotOpenCredit:int = obj["TotOpenCredit"]
      """  Total Credit based on CredInc flags  """  
      self.TotGlbInvoiceCredit:int = obj["TotGlbInvoiceCredit"]
      """  Total Global Invoice Credit (including current company)  """  
      self.TotGlbOrderCredit:int = obj["TotGlbOrderCredit"]
      """  Total Global Order Credit (including current company)  """  
      self.TotGlbPICredit:int = obj["TotGlbPICredit"]
      """  Total Global Payment Instruments Credit (including current company)  """  
      self.TotGlbOpenCredit:int = obj["TotGlbOpenCredit"]
      """  Total Global Open Credit (based on GlbCredInc flags)  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Customer is Global (master or linked)  """  
      self.PIFlag:bool = obj["PIFlag"]
      """  Indicates whether PI fields should be enabled or not  """  
      self.ApplyHoldToOrders:bool = obj["ApplyHoldToOrders"]
      """  Apply credit hold status to orders  """  
      self.FxdTotOrders:int = obj["FxdTotOrders"]
      self.FxdTotPI:int = obj["FxdTotPI"]
      self.FxdOrderCredit:int = obj["FxdOrderCredit"]
      self.FxdPICredit:int = obj["FxdPICredit"]
      self.FxdGlbOrdCredit:int = obj["FxdGlbOrdCredit"]
      self.FxdGlbPICredit:int = obj["FxdGlbPICredit"]
      self.DspGlobalCredIncOrd:bool = obj["DspGlobalCredIncOrd"]
      """  Same value as GlobalCredIncOrd except if customer not global, value is no.  """  
      self.EDITest:bool = obj["EDITest"]
      self.EDITranslator:str = obj["EDITranslator"]
      self.NAOwnCreditAvail:int = obj["NAOwnCreditAvail"]
      """  Own Credit Available  """  
      self.NAOwnCreditUsedDsp:int = obj["NAOwnCreditUsedDsp"]
      self.NAParentCrdAvail:int = obj["NAParentCrdAvail"]
      """  Available Parent?s Credit in National Accout  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      self.NASharedCreditUsedDsp:int = obj["NASharedCreditUsedDsp"]
      self.NAPoolCrdAvail:int = obj["NAPoolCrdAvail"]
      """  Available credit from credit pools to be used by this customer in National account.  """  
      self.NAChildCrdAvail:int = obj["NAChildCrdAvail"]
      """  Customer?s credit available to be shared with his Children in National Account  """  
      self.NAParentsCreditUsedDsp:int = obj["NAParentsCreditUsedDsp"]
      self.GlbNAChildCrdAvail:int = obj["GlbNAChildCrdAvail"]
      """  Global Shared Credit Available  """  
      self.GlbNAOwnCreditUsedDsp:int = obj["GlbNAOwnCreditUsedDsp"]
      self.GlbNAParentCrdAvail:int = obj["GlbNAParentCrdAvail"]
      """  Global Parents Credit Available  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      self.GlbNAParentsCreditUsedDsp:int = obj["GlbNAParentsCreditUsedDsp"]
      self.GlbNAPoolCrdAvail:int = obj["GlbNAPoolCrdAvail"]
      self.GlbNASharedCreditUsedDsp:int = obj["GlbNASharedCreditUsedDsp"]
      self.GlbNAOwnCreditAvail:int = obj["GlbNAOwnCreditAvail"]
      """  Global Own Credit Available  """  
      self.NACreditUpdated:bool = obj["NACreditUpdated"]
      """  National Credit data has been updated and recalculation is needed  """  
      self.NATotalCreditAvail:int = obj["NATotalCreditAvail"]
      """  Total Credit available in the National Account  """  
      self.NATotalCreditUsed:int = obj["NATotalCreditUsed"]
      self.NACreditCust:bool = obj["NACreditCust"]
      """  Is the customer in the National Account of Credit Checking  """  
      self.TotLCCredit:int = obj["TotLCCredit"]
      self.TotLCOpenOrders:int = obj["TotLCOpenOrders"]
      """  Total open order value against LC/ECG  """  
      self.TotLCCumInvoices:int = obj["TotLCCumInvoices"]
      """  Total cumulative invoices against LC/ECG  """  
      self.TotLCInvoiceBal:int = obj["TotLCInvoiceBal"]
      """  Total invoice balance against LC/ECG  """  
      self.TotLCUsed:int = obj["TotLCUsed"]
      """  Total LC/ECG credit used.  """  
      self.TotOpenLC:int = obj["TotOpenLC"]
      """  Total number of open LC/ECG.  """  
      self.TotOpenOrderLC:int = obj["TotOpenOrderLC"]
      """  Total number of open orders against LC/ECG.  """  
      self.TotOpenInvoicesLC:int = obj["TotOpenInvoicesLC"]
      """  Total number of open invoices against LC/ECG.  """  
      self.CollectionsChanged:bool = obj["CollectionsChanged"]
      """   Indicates ift the Collections was changed by the user but not posted yet.
Used in Peru localization.  """  
      self.CollectionsPostVisible:bool = obj["CollectionsPostVisible"]
      """   Indicates if Post Collections option in Actions menu is supposed to be visible.
Post Collections is used by Peru Localization  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AgingCreditDescription:str = obj["AgingCreditDescription"]
      self.GlobalCurrencyCurrDesc:str = obj["GlobalCurrencyCurrDesc"]
      self.GlobalCurrencyDocumentDesc:str = obj["GlobalCurrencyDocumentDesc"]
      self.GlobalCurrencyCurrName:str = obj["GlobalCurrencyCurrName"]
      self.GlobalCurrencyCurrSymbol:str = obj["GlobalCurrencyCurrSymbol"]
      self.GlobalCurrencyCurrencyID:str = obj["GlobalCurrencyCurrencyID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CMOrderHedRow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Credit Hold flag to indicate when to override credit and set limit.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TermsCode:str = obj["TermsCode"]
      """   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  """  
      self.OrderTotal:int = obj["OrderTotal"]
      """  Order Total  """  
      self.OrderBalance:int = obj["OrderBalance"]
      """  Open Order Balance  """  
      self.DepositBal:int = obj["DepositBal"]
      """  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this order.  """  
      self.CreditOverrideLimit:int = obj["CreditOverrideLimit"]
      """  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.TotalCharges:int = obj["TotalCharges"]
      """   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalMisc:int = obj["TotalMisc"]
      """   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalDiscount:int = obj["TotalDiscount"]
      """   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  """  
      self.TotalAdvBill:int = obj["TotalAdvBill"]
      """  Total Advance Billable Balance  """  
      self.TotalTax:int = obj["TotalTax"]
      """   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  """  
      self.TotalInvoiced:int = obj["TotalInvoiced"]
      """  Total amount of order that has been invoiced  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OrderOpenCredit:int = obj["OrderOpenCredit"]
      """  OrderOpenCredit  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CMOrderHedTableset:
   def __init__(self, obj):
      self.CMOrderHed:list[Erp_Tablesets_CMOrderHedRow] = obj["CMOrderHed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  """  
      self.TranType:str = obj["TranType"]
      """   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger Module.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.TranAmt:int = obj["TranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.Discount:int = obj["Discount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  """  
      self.Reference:str = obj["Reference"]
      """  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.DebitNote:bool = obj["DebitNote"]
      """  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  """  
      self.DNComments:str = obj["DNComments"]
      """  Debit Note Detail Comments.  """  
      self.DNAmount:int = obj["DNAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DocDnAmount:int = obj["DocDnAmount"]
      """  The total debit note value applied for the invoice selected for the payment during the payment transaction.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  The Debit Note Number assigned by the customer.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1DnAmount:int = obj["Rpt1DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt2DnAmount:int = obj["Rpt2DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt3DnAmount:int = obj["Rpt3DnAmount"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt No. (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date  (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate No. (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.SEPADDMsgID:str = obj["SEPADDMsgID"]
      """  SEPADDMsgID  """  
      self.SEPADDPmtID:str = obj["SEPADDPmtID"]
      """  SEPADDPmtID  """  
      self.PmtDueDate:str = obj["PmtDueDate"]
      """  PmtDueDate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MX Payment Number for AR Invoice  """  
      self.WriteOffHeadNumRef:int = obj["WriteOffHeadNumRef"]
      """  Reference to HeadNum of main CashHead record.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.TaxableAdjustment:bool = obj["TaxableAdjustment"]
      """  Taxable Adjustment  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BaseAdjAmt:int = obj["BaseAdjAmt"]
      """  Adjustment amount in Base Currency  """  
      self.BaseCurrDesc:str = obj["BaseCurrDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BillConNum:int = obj["BillConNum"]
      """  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  """  
      self.CopyRate:bool = obj["CopyRate"]
      """  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyDescription:str = obj["CurrencyDescription"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol  """  
      self.DebitNotesApplied:str = obj["DebitNotesApplied"]
      """  This field displays all Debit Note customer defined numbers applied.  """  
      self.DispDocSelfAssessAmt:int = obj["DispDocSelfAssessAmt"]
      self.DispDocWithholdAmt:int = obj["DispDocWithholdAmt"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display gl account  """  
      self.DispSelfAssessAmt:int = obj["DispSelfAssessAmt"]
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DispWithholdAmt:int = obj["DispWithholdAmt"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Doc Invoice Amount  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Doc Invoice Balance  """  
      self.DocNetCash:int = obj["DocNetCash"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      """  Doc New Invoice Balance  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  Write Off Amount  """  
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then CopyRate checkbox is Read Only  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Legal Number Field  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Legal Number Field  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GLRefCodeDesc:str = obj["GLRefCodeDesc"]
      """  G/L Reference Code Description  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Legal Number Field  """  
      self.InvDiscountDate:str = obj["InvDiscountDate"]
      self.InvDueDate:str = obj["InvDueDate"]
      self.InvExchRate:int = obj["InvExchRate"]
      """  Invoice Exchange Rate  """  
      self.InvLegalNumber:str = obj["InvLegalNumber"]
      self.InvLockRate:bool = obj["InvLockRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Invoice Amount  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.InvTermsCode:str = obj["InvTermsCode"]
      self.InvXRateLabel:str = obj["InvXRateLabel"]
      self.IsCreditPayment:bool = obj["IsCreditPayment"]
      """  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  """  
      self.IsDiscountforCreditM:bool = obj["IsDiscountforCreditM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      self.NetCash:int = obj["NetCash"]
      self.NewBalance:int = obj["NewBalance"]
      """  New Invoice Balance  """  
      self.OldGainLoss:int = obj["OldGainLoss"]
      self.OrderNum:int = obj["OrderNum"]
      """  The related order number (InvcHead.OrderNum)  """  
      self.PNRef:str = obj["PNRef"]
      """  Processing company's Reference ID, unique to each transaction  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions  """  
      self.RecalcTranAmt:bool = obj["RecalcTranAmt"]
      """  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  """  
      self.RedStornoOpt:str = obj["RedStornoOpt"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.RemoveForAdjustment:bool = obj["RemoveForAdjustment"]
      """  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt1NetCash:int = obj["Rpt1NetCash"]
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt1OldGainLoss:int = obj["Rpt1OldGainLoss"]
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1WriteOffGainLossAmt:int = obj["Rpt1WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt2NetCash:int = obj["Rpt2NetCash"]
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt2OldGainLoss:int = obj["Rpt2OldGainLoss"]
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2WriteOffGainLossAmt:int = obj["Rpt2WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.Rpt3NetCash:int = obj["Rpt3NetCash"]
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.Rpt3OldGainLoss:int = obj["Rpt3OldGainLoss"]
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3WriteOffGainLossAmt:int = obj["Rpt3WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with CashDtl.SoldToCustNum  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  Populated from InvcHead.SoldToCustNum.  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  CustName associated with CashDtl.SoldToCustNum  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  Legal Number Field  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of the Tran Type  """  
      self.Type:str = obj["Type"]
      """  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  """  
      self.WriteOff:bool = obj["WriteOff"]
      """  Write Off  """  
      self.WriteOffAccount:str = obj["WriteOffAccount"]
      """  Write Off Account  """  
      self.WriteOffAccountDesc:str = obj["WriteOffAccountDesc"]
      """  Write Off Account Description  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffGainLossAmt:int = obj["WriteOffGainLossAmt"]
      """  Write Off Gain Loss Amount  """  
      self.XRateLabel:str = obj["XRateLabel"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Legal Number Field  """  
      self.OldWriteOffAmount:int = obj["OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffAccountDisp:str = obj["WriteOffAccountDisp"]
      self.TaxableWriteOff:bool = obj["TaxableWriteOff"]
      self.TotalGainLossAmt:int = obj["TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.OldWriteOffGainLossAmt:int = obj["OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffGainLossAmt:int = obj["Rpt1OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffGainLossAmt:int = obj["Rpt2OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffGainLossAmt:int = obj["Rpt3OldWriteOffGainLossAmt"]
      """  Write Off Amount  """  
      self.Rpt1TotalGainLossAmt:int = obj["Rpt1TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt2TotalGainLossAmt:int = obj["Rpt2TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.Rpt3TotalGainLossAmt:int = obj["Rpt3TotalGainLossAmt"]
      """  Total Gain Loss Amount  """  
      self.DocOldWriteOffAmount:int = obj["DocOldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt1OldWriteOffAmount:int = obj["Rpt1OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt2OldWriteOffAmount:int = obj["Rpt2OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.Rpt3OldWriteOffAmount:int = obj["Rpt3OldWriteOffAmount"]
      """  Write Off Amount  """  
      self.WriteOffComment:str = obj["WriteOffComment"]
      """  Allows uset to enter comment for Write Off.  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding amount tax was manually modified.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumInvoiceType:str = obj["InvoiceNumInvoiceType"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashDtlTableset:
   def __init__(self, obj):
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CashHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Displays the ID of the group the transaction is assigned to.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Displays the receipt header number used for internal reference.  """  
      self.Posted:bool = obj["Posted"]
      """  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  """  
      self.TranType:str = obj["TranType"]
      """  Displays the transaction type.  """  
      self.CheckRef:str = obj["CheckRef"]
      """  Displays the number of the check.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Displays the transaction amount.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Displays the transaction amount in customer currency.  """  
      self.CustID:str = obj["CustID"]
      """  Displays the customer ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  Displays the date of the transaction.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  """  
      self.UnAppliedAmt:int = obj["UnAppliedAmt"]
      """  Displays the unapplied amount.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Displays the unapplied amount in base currency.  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Displays the amount applied to invoices.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Displays the amount in document currency applied to invoices.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Displays the fiscal year that the check is posted to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Displays the fiscal period that the check is posted to.  """  
      self.Reference:str = obj["Reference"]
      """  Displays any reference.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted.  """  
      self.CreditMemoNum:int = obj["CreditMemoNum"]
      """  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Displays the customer currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Displays the exchange rate that is used for this check.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Displays the tax amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Displays the legal number of the check.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GLRefType:str = obj["GLRefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.GLRefCode:str = obj["GLRefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.CCAmount:int = obj["CCAmount"]
      """  Credit Transaction Amount, makes up part of CCTotal  """  
      self.CCFreight:int = obj["CCFreight"]
      """  Credit Card transaction freight amount, part of CCTotal  """  
      self.CCTax:int = obj["CCTax"]
      """  Credit Card Transaction Tax amount, part of CCTotal  """  
      self.CCTotal:int = obj["CCTotal"]
      """  Total amount being sent to the credit card processor  """  
      self.CCDocAmount:int = obj["CCDocAmount"]
      """  See CCAmount  """  
      self.CCDocFreight:int = obj["CCDocFreight"]
      """  See CCFreight  """  
      self.CCDocTax:int = obj["CCDocTax"]
      """  See CCTax  """  
      self.CCDocTotal:int = obj["CCDocTotal"]
      """  See CCTotal  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnAppliedAmt:int = obj["Rpt1UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnAppliedAmt:int = obj["Rpt2UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnAppliedAmt:int = obj["Rpt3UnAppliedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1CCAmount:int = obj["Rpt1CCAmount"]
      """  See CCAmount  """  
      self.Rpt2CCAmount:int = obj["Rpt2CCAmount"]
      """  See CCAmount  """  
      self.Rpt3CCAmount:int = obj["Rpt3CCAmount"]
      """  See CCAmount  """  
      self.Rpt1CCFreight:int = obj["Rpt1CCFreight"]
      """  See CCFreight  """  
      self.Rpt2CCFreight:int = obj["Rpt2CCFreight"]
      """  See CCFreight  """  
      self.Rpt3CCFreight:int = obj["Rpt3CCFreight"]
      """  See CCFreight  """  
      self.Rpt1CCTax:int = obj["Rpt1CCTax"]
      """  See CCTax  """  
      self.Rpt2CCTax:int = obj["Rpt2CCTax"]
      """  See CCTax  """  
      self.Rpt3CCTax:int = obj["Rpt3CCTax"]
      """  See CCTax  """  
      self.Rpt1CCTotal:int = obj["Rpt1CCTotal"]
      """  See CCTotal  """  
      self.Rpt2CCTotal:int = obj["Rpt2CCTotal"]
      """  See CCTotal  """  
      self.Rpt3CCTotal:int = obj["Rpt3CCTotal"]
      """  See CCTotal  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.ReceiptCurrencyCode:str = obj["ReceiptCurrencyCode"]
      """  The unique code of Receipt Currency.  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  Amount of Receipt in Receipt Currency.  """  
      self.BankRcptExchangeRate:int = obj["BankRcptExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  """  
      self.SettlementExchangeRate:int = obj["SettlementExchangeRate"]
      """  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  """  
      self.CMCurrencyCode:str = obj["CMCurrencyCode"]
      """  The unique Currency code for Credit Memo.  """  
      self.CMAmount:int = obj["CMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.ReverseRef:int = obj["ReverseRef"]
      """  Reference to cash receipt which had been reversed.  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Date when cash receipt had been reversed  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.TaxWhld:int = obj["TaxWhld"]
      """  Withhold Tax  """  
      self.DiscountDate:str = obj["DiscountDate"]
      """  Dsicount Date  """  
      self.TaxWhldCalc:int = obj["TaxWhldCalc"]
      """  Calculate Withhold Tax  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.UnallocatedAmt:int = obj["UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  """  
      self.DocUnallocatedAmt:int = obj["DocUnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  """  
      self.Rpt1UnallocatedAmt:int = obj["Rpt1UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  """  
      self.Rpt2UnallocatedAmt:int = obj["Rpt2UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  """  
      self.Rpt3UnallocatedAmt:int = obj["Rpt3UnallocatedAmt"]
      """  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  """  
      self.ApplyHeadNum:int = obj["ApplyHeadNum"]
      """  Number of the unallocated deposit payment to be apply.  """  
      self.AllocatedAmt:int = obj["AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Base currency.  """  
      self.DocAllocatedAmt:int = obj["DocAllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Document currency.  """  
      self.Rpt1AllocatedAmt:int = obj["Rpt1AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  """  
      self.Rpt2AllocatedAmt:int = obj["Rpt2AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  """  
      self.Rpt3AllocatedAmt:int = obj["Rpt3AllocatedAmt"]
      """  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  """  
      self.Comment:str = obj["Comment"]
      """  Comments related to the cash receipt.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.TaxRemarks:str = obj["TaxRemarks"]
      """  Tax Remarks  """  
      self.NonDeductCode:str = obj["NonDeductCode"]
      """  Non Deductable Code  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.MandateReference:str = obj["MandateReference"]
      """  MandateReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SEPADDExportDate:str = obj["SEPADDExportDate"]
      """  SEPADDExportDate  """  
      self.BOEInvoiceNum:int = obj["BOEInvoiceNum"]
      """  BOE Invoice Number  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.DocumentType:str = obj["DocumentType"]
      """  DocumentType  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.BankRcptExchangeRate10D:int = obj["BankRcptExchangeRate10D"]
      """  BankRcptExchangeRate10D  """  
      self.SettlementExchangeRate10D:int = obj["SettlementExchangeRate10D"]
      """  SettlementExchangeRate10D  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.RcptCurAppliedAmt:int = obj["RcptCurAppliedAmt"]
      """  The amount of the cash receipt applied to invoices in receipt currency  """  
      self.RcptCurUnAppliedAmt:int = obj["RcptCurUnAppliedAmt"]
      """  The amount of the cash receipt that is unapplied in receipt currency  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MX Method of Payment: single, multiple, etc.  """  
      self.MXPaySupplementFlag:bool = obj["MXPaySupplementFlag"]
      """  If TRUE then MX Electronic Payment XML is required  """  
      self.LockboxID:str = obj["LockboxID"]
      """  LockboxID  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MX Receipt’s Fiscal Folio (UUID)  """  
      self.MXOriginalCheckRef:str = obj["MXOriginalCheckRef"]
      """  MX UUID of the original Receipt being corrected  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MX Confirmation Code for special Cash Receipts  """  
      self.MXBankID:str = obj["MXBankID"]
      """  MX Customer’s Bank ID  """  
      self.ReversedReason:str = obj["ReversedReason"]
      """  Text entered by the user to indicate the reason Cash receipt was Reversed.  """  
      self.CCCity:str = obj["CCCity"]
      """  Credit Card Holder City.  """  
      self.CCState:str = obj["CCState"]
      """  Credit Card Holder State.  """  
      self.ccToken:str = obj["ccToken"]
      """  ccToken  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.Adjustment:bool = obj["Adjustment"]
      """  Indicates this record is an adjustment CashHead.  """  
      self.AdjustmentRef:int = obj["AdjustmentRef"]
      """  Reference to cash receipt which had been adjusted.  """  
      self.AdjustmentReason:str = obj["AdjustmentReason"]
      """  The reason for the adjustment entered by the user  """  
      self.WriteOffAmount:int = obj["WriteOffAmount"]
      """  Total Check Write Off Amount  """  
      self.DocWriteOffAmount:int = obj["DocWriteOffAmount"]
      """  DocWriteOffAmount  """  
      self.Rpt1WriteOffAmount:int = obj["Rpt1WriteOffAmount"]
      """  Rpt1WriteOffAmount  """  
      self.Rpt2WriteOffAmount:int = obj["Rpt2WriteOffAmount"]
      """  Rpt2WriteOffAmount  """  
      self.Rpt3WriteOffAmount:int = obj["Rpt3WriteOffAmount"]
      """  Rpt3WriteOffAmount  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Mexico Certified Timestamp  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  Mexico SAT Seal  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Mexico Digital Seal  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  Mexico SAT Certificate Serial Number  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  Mexico Original String Timbre Fiscal Digital  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Mexico Certificate  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Mexico Certificate Serial Number  """  
      self.SourceGroupID:str = obj["SourceGroupID"]
      """  SourceGroupID  """  
      self.SourceHeadNum:int = obj["SourceHeadNum"]
      """  SourceHeadNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.CustomerBankID:str = obj["CustomerBankID"]
      """  ID of the Customer's bank.  """  
      self.CustomerBankAcctNumber:str = obj["CustomerBankAcctNumber"]
      """  The Bank account number for the Customer.  """  
      self.CustomerBankSwiftNum:str = obj["CustomerBankSwiftNum"]
      """  CustomerBankSwiftNum  """  
      self.CustomerBankIBANCode:str = obj["CustomerBankIBANCode"]
      """  The Bank account IBAN Code  """  
      self.CustomerBankNameOnAccount:str = obj["CustomerBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.CustomerBankAddress1:str = obj["CustomerBankAddress1"]
      """  First address line of customer bank.  """  
      self.CustomerBankAddress2:str = obj["CustomerBankAddress2"]
      """  Second address line of customer bank.  """  
      self.CustomerBankAddress3:str = obj["CustomerBankAddress3"]
      """  Third address line of customer bank.  """  
      self.CustomerBankCity:str = obj["CustomerBankCity"]
      """  Bank City  """  
      self.CustomerBankState:str = obj["CustomerBankState"]
      """  Bank State/Prov  """  
      self.CustomerBankPostalCode:str = obj["CustomerBankPostalCode"]
      """  Postal Code or zip code  """  
      self.CustomerBankCountryNum:int = obj["CustomerBankCountryNum"]
      """  Bank account Country Number.  """  
      self.ARRemittanceSlipPrinted:bool = obj["ARRemittanceSlipPrinted"]
      """  ARRemittanceSlipPrinted  """  
      self.CustomerBankName:str = obj["CustomerBankName"]
      """  Customer Bank Name  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXEPaymentType:str = obj["MXEPaymentType"]
      """  MXEPaymentType  """  
      self.MXEPaymentCertificateNumber:str = obj["MXEPaymentCertificateNumber"]
      """  MXEPaymentCertificateNumber  """  
      self.MXEPaymentOriginalString:str = obj["MXEPaymentOriginalString"]
      """  MXEPaymentOriginalString  """  
      self.MXEPaymentDigitalSeal:str = obj["MXEPaymentDigitalSeal"]
      """  MXEPaymentDigitalSeal  """  
      self.Source:str = obj["Source"]
      """  Source  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  GL Description for the Reverse process  """  
      self.CMDescription:str = obj["CMDescription"]
      """  GL Description for AR - Apply Credit Memo  """  
      self.BankReceiptAmt:int = obj["BankReceiptAmt"]
      """  Receipt Amount in Bank Currency  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstHeadNum:int = obj["MXSubstHeadNum"]
      """  MXSubstHeadNum  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  E-invoice Service Provider Status  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  E-invoice Status  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  E-invoice Updated On  """  
      self.AdjustmentCustName:str = obj["AdjustmentCustName"]
      """  Adjustment Customer Name  """  
      self.AdjustmentCustNum:int = obj["AdjustmentCustNum"]
      """  Customer to which the new invoices will be applied.  """  
      self.AdjustmentDate:str = obj["AdjustmentDate"]
      """  Date the adjustment was made.  """  
      self.AdjustmentDocUnAppliedAmt:int = obj["AdjustmentDocUnAppliedAmt"]
      """  Displays the amount available to apply to the invoices.  """  
      self.AdjustmentOnAccount:bool = obj["AdjustmentOnAccount"]
      """  On Account  """  
      self.AdjustmentTranDocTypeID:str = obj["AdjustmentTranDocTypeID"]
      """  Temp TranDocTypeID used when adjusting a Cash Rececipt  """  
      self.AllocDepBal:int = obj["AllocDepBal"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      self.AllowUpdSettlementCurr:bool = obj["AllowUpdSettlementCurr"]
      """  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  """  
      self.AmtToAlloc:int = obj["AmtToAlloc"]
      """  Amount to Allocate  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.AVSAddr:str = obj["AVSAddr"]
      """  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.AVSZip:str = obj["AVSZip"]
      """  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Currency Value  """  
      self.BankBaseXRateLabel:str = obj["BankBaseXRateLabel"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      """  Bank Currency Symbol  """  
      self.BankExchangeRate:int = obj["BankExchangeRate"]
      self.BankRcptXRateLabel:str = obj["BankRcptXRateLabel"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Base Currency Symbol  """  
      self.BillToName:str = obj["BillToName"]
      """  Bill To Name  """  
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  """  
      self.CardStore:str = obj["CardStore"]
      """  Stored Credit Card Number  """  
      self.CCAllowSales:bool = obj["CCAllowSales"]
      """  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  """  
      self.CCApprovalNum:str = obj["CCApprovalNum"]
      self.CCCSCID:str = obj["CCCSCID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  """  
      self.CCCSCIDToken:str = obj["CCCSCIDToken"]
      """  Tokenized value of CSCID  """  
      self.CCEnableAddress:bool = obj["CCEnableAddress"]
      """  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  """  
      self.CCEnableCSC:bool = obj["CCEnableCSC"]
      """  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  """  
      self.CCIsTraining:bool = obj["CCIsTraining"]
      """   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  """  
      self.CCResponse:str = obj["CCResponse"]
      """  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  """  
      self.CCTranID:str = obj["CCTranID"]
      """  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  """  
      self.CCTranType:str = obj["CCTranType"]
      """  Credit Card Transaction Type  """  
      self.CentralCollectionCheck:bool = obj["CentralCollectionCheck"]
      """  Check Box on the UI to filter records by Central Collection flag  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  """  
      self.CREProcessor:bool = obj["CREProcessor"]
      """  CREProcessor is true when Credit Card Configuration is CRE Server.  """  
      self.CSCResult:str = obj["CSCResult"]
      """  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  """  
      self.CurrAmtSelected:int = obj["CurrAmtSelected"]
      """  Current Amount Selected on Invoice Select Tab  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustFullAddr:str = obj["CustFullAddr"]
      """  Displays the address of the customer that paid the receipt.  """  
      self.CustomerName:str = obj["CustomerName"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocAllocDepBal:int = obj["DocAllocDepBal"]
      self.DocAmtToAlloc:int = obj["DocAmtToAlloc"]
      """  Doc Amount to Allocate  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Displays the discount applied to the receipt.  """  
      self.DocReceipt:int = obj["DocReceipt"]
      """  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  """  
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.DocumentNum:int = obj["DocumentNum"]
      """  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  """  
      self.DocWhldTax:int = obj["DocWhldTax"]
      self.DspBankBatchID:str = obj["DspBankBatchID"]
      self.DspCMAmount:int = obj["DspCMAmount"]
      """  Amount of Credit Memo in CM Currency.  """  
      self.DspDocTranAmt:int = obj["DspDocTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.DspSalesOrderValue:int = obj["DspSalesOrderValue"]
      self.DspTranAmt:int = obj["DspTranAmt"]
      """  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      self.EnableGetDefaultAcct:bool = obj["EnableGetDefaultAcct"]
      """  Indicates if the option to get the default account is enable.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      self.EnableTransactionDate:bool = obj["EnableTransactionDate"]
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.GLRefCodeDescription:str = obj["GLRefCodeDescription"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      self.InvcLegalNumber:str = obj["InvcLegalNumber"]
      """  The InvcHead legal number  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberDsp:str = obj["LegalNumberDsp"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockRate:bool = obj["LockRate"]
      """  Copied from OrderHed.LockRate  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      self.MXECEPXml:str = obj["MXECEPXml"]
      """  MXECEPXml  """  
      self.MXOriginalRefNum:str = obj["MXOriginalRefNum"]
      """  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  """  
      self.ReferencePNRef:str = obj["ReferencePNRef"]
      """  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  """  
      self.Rpt1AllocDepBal:int = obj["Rpt1AllocDepBal"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1WhldTax:int = obj["Rpt1WhldTax"]
      self.Rpt2AllocDepBal:int = obj["Rpt2AllocDepBal"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt2WhldTax:int = obj["Rpt2WhldTax"]
      self.Rpt3AllocDepBal:int = obj["Rpt3AllocDepBal"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt3WhldTax:int = obj["Rpt3WhldTax"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesOrderValue:int = obj["SalesOrderValue"]
      self.SettlementXRateLabel:str = obj["SettlementXRateLabel"]
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  """  
      self.SystemTranType:str = obj["SystemTranType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Description of TranType  """  
      self.UnappliedAmountApplied:bool = obj["UnappliedAmountApplied"]
      """  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  """  
      self.WhldTax:int = obj["WhldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AdjustmentCustID:str = obj["AdjustmentCustID"]
      """  Displays the customer ID.  """  
      self.ReferenceTranDate:str = obj["ReferenceTranDate"]
      self.ReferenceTranNum:int = obj["ReferenceTranNum"]
      self.ReferenceTranTime:int = obj["ReferenceTranTime"]
      self.CustFullAddrFormatted:str = obj["CustFullAddrFormatted"]
      """  Displays the address of the customer that paid the receipt with newline delimiter.  """  
      self.EnableManualWHTax:bool = obj["EnableManualWHTax"]
      """  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  """  
      self.WHTaxManualChange:bool = obj["WHTaxManualChange"]
      """  Indicates if the withholding tax was manually modified.  """  
      self.TranTypeDescCaption:str = obj["TranTypeDescCaption"]
      """  Payment type description, displayed in the Details page header.  """  
      self.AdjustmentCustAddress:str = obj["AdjustmentCustAddress"]
      self.MXSubstGroupId:str = obj["MXSubstGroupId"]
      """  Substitution Cash Receipt Group ID  """  
      self.MXSubstCheckRef:str = obj["MXSubstCheckRef"]
      """  Substitution Cash Receipt CheckRef  """  
      self.MXSubstFiscalFolio:str = obj["MXSubstFiscalFolio"]
      """  Substitution Cash Receipt UUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CashBHedPosted:bool = obj["CashBHedPosted"]
      self.CashBHedCashBookNum:int = obj["CashBHedCashBookNum"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CMCurrencyCodeDocumentDesc:str = obj["CMCurrencyCodeDocumentDesc"]
      self.CMCurrencyCodeCurrName:str = obj["CMCurrencyCodeCurrName"]
      self.CMCurrencyCodeCurrSymbol:str = obj["CMCurrencyCodeCurrSymbol"]
      self.CMCurrencyCodeCurrDesc:str = obj["CMCurrencyCodeCurrDesc"]
      self.CMCurrencyCodeCurrencyID:str = obj["CMCurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PCashDocDirection:str = obj["PCashDocDirection"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.PMUIDMXSATCode:str = obj["PMUIDMXSATCode"]
      self.PMUIDSummarizePerCustomer:bool = obj["PMUIDSummarizePerCustomer"]
      self.PMUIDType:int = obj["PMUIDType"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.RcptCurrencyCodeCurrencyID:str = obj["RcptCurrencyCodeCurrencyID"]
      self.RcptCurrencyCodeDocumentDesc:str = obj["RcptCurrencyCodeDocumentDesc"]
      self.RcptCurrencyCodeCurrDesc:str = obj["RcptCurrencyCodeCurrDesc"]
      self.RcptCurrencyCodeCurrSymbol:str = obj["RcptCurrencyCodeCurrSymbol"]
      self.RcptCurrencyCodeCurrName:str = obj["RcptCurrencyCodeCurrName"]
      self.ReverseMXCancelReasonCode:str = obj["ReverseMXCancelReasonCode"]
      self.ReverseMXCancellationMode:str = obj["ReverseMXCancellationMode"]
      self.SourceTranDateTranDate:str = obj["SourceTranDateTranDate"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CashHeadTableset:
   def __init__(self, obj):
      self.CashHead:list[Erp_Tablesets_CashHeadRow] = obj["CashHead"]
      self.CashDtl:list[Erp_Tablesets_CashDtlRow] = obj["CashDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CreditManagerTableset:
   def __init__(self, obj):
      self.CMCustomer:list[Erp_Tablesets_CMCustomerRow] = obj["CMCustomer"]
      self.CustomCrdPool:list[Erp_Tablesets_CustomCrdPoolRow] = obj["CustomCrdPool"]
      self.GlbCustCred:list[Erp_Tablesets_GlbCustCredRow] = obj["GlbCustCred"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustNum:int = obj["CustNum"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.ConNum:int = obj["ConNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo.ShipToNum of the Ship To that the customer  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.SpecialAddress:bool = obj["SpecialAddress"]
      """  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  """  
      self.Address1:str = obj["Address1"]
      """  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  """  
      self.Address2:str = obj["Address2"]
      """  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.Address3:str = obj["Address3"]
      """  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  """  
      self.City:str = obj["City"]
      """  The city portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.State:str = obj["State"]
      """  The state or province portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.Country:str = obj["Country"]
      """  The Country portion of the contact's mailing address. (See Address1 for additional information).  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value of the country selected for the contact's mailing address.  """  
      self.SFPortalPassword:str = obj["SFPortalPassword"]
      """  Customer Connect password for this contact.  """  
      self.SFUser:bool = obj["SFUser"]
      """  Indicates if able to create Orders  """  
      self.PortalUser:bool = obj["PortalUser"]
      """  Indicates if "Order History" is functional  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates whether or not this contact should be included in marketing lists.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that the contact was entered into the database.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserFile.DCDUserID of the user that entered the contact into the database.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  **NOTE cannot find any code that maintains this field.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External ID  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record receives global updates  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.MasterCustNum:int = obj["MasterCustNum"]
      """  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterShipToNum:str = obj["MasterShipToNum"]
      """  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.MasterConNum:int = obj["MasterConNum"]
      """  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.PerConAddress:bool = obj["PerConAddress"]
      """  Indicates if the Person/Contact address should be used as the Special Quoting Address.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  This field defines if the customer contact  is synchronized to an External CRM.  """  
      self.ExternalCRMCustomerID:str = obj["ExternalCRMCustomerID"]
      """  This field holds the id of this customer in the External CRM  """  
      self.ExternalCRMContactID:str = obj["ExternalCRMContactID"]
      """  This field holds the id of this customer contact in the External CRM  """  
      self.RoleDescription:str = obj["RoleDescription"]
      self.PrimaryBilling:bool = obj["PrimaryBilling"]
      """   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  """  
      self.PrimaryPurchasing:bool = obj["PrimaryPurchasing"]
      """   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  """  
      self.PrimaryShipping:bool = obj["PrimaryShipping"]
      """   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Contact is global (Master or Linked)  """  
      self.AttrCodeList:str = obj["AttrCodeList"]
      """  delimited list of CustCnAttr codes  """  
      self.GlbLink:str = obj["GlbLink"]
      """  GlbCustCnt fields in a linked list to find the linking record  """  
      self.ContactName:str = obj["ContactName"]
      """  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.MasterCustNumBTName:str = obj["MasterCustNumBTName"]
      self.MasterCustNumName:str = obj["MasterCustNumName"]
      self.MasterCustNumCustID:str = obj["MasterCustNumCustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustCntTableset:
   def __init__(self, obj):
      self.CustCnt:list[Erp_Tablesets_CustCntRow] = obj["CustCnt"]
      self.CustCntAttch:list[Erp_Tablesets_CustCntAttchRow] = obj["CustCntAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustomCrdPoolRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CustNum:int = obj["CustNum"]
      self.CrdPoolCode:str = obj["CrdPoolCode"]
      self.CreditUsed:int = obj["CreditUsed"]
      self.CreditAvailable:int = obj["CreditAvailable"]
      self.GlobalNA:bool = obj["GlobalNA"]
      """  Global Pool - shows if the pool belongs to Global National Account  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExportCustCredRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Customer Type  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name  """  
      self.CreditLimit:int = obj["CreditLimit"]
      """  Credit Limit  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Credit Review Date stored as character  """  
      self.InvoiceCreditTot:int = obj["InvoiceCreditTot"]
      """  Total invoice credit amount  """  
      self.OrderCreditTot:int = obj["OrderCreditTot"]
      """  Total order credit amount  """  
      self.CreditTot:int = obj["CreditTot"]
      """  Total credit amount  """  
      self.NumInvoice:int = obj["NumInvoice"]
      """  Total number of invoices  """  
      self.NumOrder:int = obj["NumOrder"]
      """  Total number of orders  """  
      self.CreditHold:int = obj["CreditHold"]
      """  Credit Hold values: 1 = Customer on credit hold; 0 = Not on hold  """  
      self.CreditIncludeOrders:int = obj["CreditIncludeOrders"]
      """  Credit Include Order values: 1 = Include Orders; 0 = Exclude Orders  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExportCustCredTableset:
   def __init__(self, obj):
      self.ExportCustCred:list[Erp_Tablesets_ExportCustCredRow] = obj["ExportCustCred"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCustCredRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  Company credit totals came from (not just owner of the global customer)  """  
      self.ExtCompName:str = obj["ExtCompName"]
      self.UpdateDate:str = obj["UpdateDate"]
      """  Date the credit was last updated  """  
      self.DocARTotal:int = obj["DocARTotal"]
      """  Open AR Credit in Global Currency  """  
      self.DocSOTotal:int = obj["DocSOTotal"]
      """  Open Order Credit in Global Currency  """  
      self.DocPITotal:int = obj["DocPITotal"]
      """  Open PI Credit in Global Currency  """  
      self.ARTotal:int = obj["ARTotal"]
      """  AR Credit in local companies base currency  """  
      self.SOTotal:int = obj["SOTotal"]
      """  SO Credit in local companies base currency  """  
      self.PITotal:int = obj["PITotal"]
      """  PI Credit in local companies base currency  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  Holds connection and exchange rate error messages  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  This field holds the associated Global Customer number.  If this is the "parent" customer then it will match the CustNum field.  0 indicates that this is not a global customer at all  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The Customer.CustNum value of the customer's parent company.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  """  
      self.TotalInvoices:int = obj["TotalInvoices"]
      """  Total Number of Open Invoices  """  
      self.TotalOrders:int = obj["TotalOrders"]
      """  Total Number of Open Orders  """  
      self.TotalPayIns:int = obj["TotalPayIns"]
      """  Total Number of open Payment Instruments  """  
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      """  Parent's Credit used by this customer  """  
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      """  Shared Credit used by children  """  
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      """  Own Credit used by himself  """  
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      """  Global Parent's Credit used by this customer  """  
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      """  Shared Credit used by Global children  """  
      self.NAPoolCreditUsed:int = obj["NAPoolCreditUsed"]
      """  Pool Credit used  """  
      self.GlbNAPoolCreditUsed:int = obj["GlbNAPoolCreditUsed"]
      """  Global Credit Pool used  """  
      self.GlbNAOwnCreditUsed:int = obj["GlbNAOwnCreditUsed"]
      """  Own Credit used by himself  """  
      self.NAExceedLimit:int = obj["NAExceedLimit"]
      """  Allocated Credit exceed Credit Limit  """  
      self.GlbNAExceedLimit:int = obj["GlbNAExceedLimit"]
      """  Allocated Credit exceed Global Credit Limit  """  
      self.ARLOCTotal:int = obj["ARLOCTotal"]
      """  AR Letter of Credit Credit in local companies base currency  """  
      self.DocARLOCTotal:int = obj["DocARLOCTotal"]
      """  Open AR Letter of Credit Credit in Global Currency  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportCustCredRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustomerType:str = obj["CustomerType"]
      self.CustName:str = obj["CustName"]
      self.CreditLimit:int = obj["CreditLimit"]
      """  Customer Credit Limit  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Credit Review Date  """  
      self.CreditHold:int = obj["CreditHold"]
      """  Credit Hold values: 1 = Customer is on hold; 0 = Not on hold  """  
      self.CreditIncludeOrders:int = obj["CreditIncludeOrders"]
      """  Credit Include Order values: 1 = Include orders; 0 = Exclude orders  """  
      self.InvoiceCreditTot:int = obj["InvoiceCreditTot"]
      """  Total invoice credit amount  """  
      self.OrderCreditTot:int = obj["OrderCreditTot"]
      """  Total order credit amount  """  
      self.CreditTot:int = obj["CreditTot"]
      """  Total credit amount  """  
      self.NumInvoice:int = obj["NumInvoice"]
      """  Total number of invoices  """  
      self.NumOrder:int = obj["NumOrder"]
      """  Total number of orders  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportCustCredTableset:
   def __init__(self, obj):
      self.ImportCustCred:list[Erp_Tablesets_ImportCustCredRow] = obj["ImportCustCred"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Indicates if invoice is "open".  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  """  
      self.CreditMemo:bool = obj["CreditMemo"]
      """   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  """  
      self.UnappliedCash:bool = obj["UnappliedCash"]
      """  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  """  
      self.CheckRef:str = obj["CheckRef"]
      """   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  """  
      self.InvoiceSuffix:str = obj["InvoiceSuffix"]
      """  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  """  
      self.GroupID:str = obj["GroupID"]
      """  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  """  
      self.DeferredRevenue:bool = obj["DeferredRevenue"]
      """  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  """  
      self.PONum:str = obj["PONum"]
      """  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  User ID that entered the invoice. This is not maintainable by the user.  """  
      self.FOB:str = obj["FOB"]
      """  Defaults from sales order ORderHed.FOB  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Once posted, maintenance is not allowed.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.UnpostedBal:int = obj["UnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.DepositCredit:int = obj["DepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.DocDepositCredit:int = obj["DocDepositCredit"]
      """  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  """  
      self.SalesRepList:str = obj["SalesRepList"]
      """  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  """  
      self.RefCancelled:int = obj["RefCancelled"]
      """  Value of this field is reference to invoice which has been cancelled by current invoice.  """  
      self.RefCancelledBy:int = obj["RefCancelledBy"]
      """  Value of this field is reference to invoice that cancelled this invoice.  """  
      self.StartUp:bool = obj["StartUp"]
      """  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  """  
      self.PayDates:str = obj["PayDates"]
      """  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayAmounts:str = obj["PayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.DocPayAmounts:str = obj["DocPayAmounts"]
      """  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  """  
      self.PayDiscDate:str = obj["PayDiscDate"]
      """  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  """  
      self.PayDiscAmt:int = obj["PayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.DocPayDiscAmt:int = obj["DocPayDiscAmt"]
      """  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  """  
      self.BillConNum:int = obj["BillConNum"]
      """  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  """  
      self.InvoiceHeld:bool = obj["InvoiceHeld"]
      """  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal that invoice was posted to.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  """  
      self.RMANum:int = obj["RMANum"]
      """   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that the invoice is relate to.  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  The member's name on the credit card.  """  
      self.CardNumber:str = obj["CardNumber"]
      """  The credit card account identifier.  """  
      self.CardType:str = obj["CardType"]
      """  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  """  
      self.ExpirationMonth:int = obj["ExpirationMonth"]
      """  The expiration month of the credit card.  """  
      self.ExpirationYear:int = obj["ExpirationYear"]
      """  The expiration year of the credit card.  """  
      self.CardID:str = obj["CardID"]
      """  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  """  
      self.CardmemberReference:str = obj["CardmemberReference"]
      """  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External Identifier  """  
      self.XRefInvoiceNum:str = obj["XRefInvoiceNum"]
      """  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.DepGainLoss:int = obj["DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.DNComments:str = obj["DNComments"]
      """  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  """  
      self.DNCustNbr:str = obj["DNCustNbr"]
      """  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  """  
      self.DebitNote:bool = obj["DebitNote"]
      """   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  """  
      self.SoldToCustNum:int = obj["SoldToCustNum"]
      """  This is populated from ShipHead.CustNum representing the Sold To customer.  """  
      self.Consolidated:bool = obj["Consolidated"]
      """  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  """  
      self.BillToInvoiceAddress:bool = obj["BillToInvoiceAddress"]
      """  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  """  
      self.SoldToInvoiceAddress:bool = obj["SoldToInvoiceAddress"]
      """  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Stores the encrypted credit card number  """  
      self.RepComm1:int = obj["RepComm1"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm2:int = obj["RepComm2"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm3:int = obj["RepComm3"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm4:int = obj["RepComm4"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepComm5:int = obj["RepComm5"]
      """  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  """  
      self.RepSales1:int = obj["RepSales1"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales2:int = obj["RepSales2"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales3:int = obj["RepSales3"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales4:int = obj["RepSales4"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSales5:int = obj["RepSales5"]
      """  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  """  
      self.CMType:str = obj["CMType"]
      """  Indicates if the Credit Memo is for a Rebate  """  
      self.CCStreetAddr:str = obj["CCStreetAddr"]
      """  Address used during AVS validation for credit transactions  """  
      self.CCZip:str = obj["CCZip"]
      """  Zip used during AVS validation in credit transactions  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.EDIReady:bool = obj["EDIReady"]
      """  Defines if this document is marked as EDI Ready  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rounding:int = obj["Rounding"]
      """  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  """  
      self.DocRounding:int = obj["DocRounding"]
      """  Rounding in Customer currency  """  
      self.Rpt1DepositCredit:int = obj["Rpt1DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2DepositCredit:int = obj["Rpt2DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3DepositCredit:int = obj["Rpt3DepositCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayAmounts:str = obj["Rpt1PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayAmounts:str = obj["Rpt2PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayAmounts:str = obj["Rpt3PayAmounts"]
      """  Reporting currency value of this field  """  
      self.Rpt1PayDiscAmt:int = obj["Rpt1PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2PayDiscAmt:int = obj["Rpt2PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3PayDiscAmt:int = obj["Rpt3PayDiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1Rounding:int = obj["Rpt1Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt2Rounding:int = obj["Rpt2Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt3Rounding:int = obj["Rpt3Rounding"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnpostedBal:int = obj["Rpt1UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnpostedBal:int = obj["Rpt2UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnpostedBal:int = obj["Rpt3UnpostedBal"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.DocDepApplied:int = obj["DocDepApplied"]
      """  Amount of deposit applied  """  
      self.Rpt1DepGainLoss:int = obj["Rpt1DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2DepGainLoss:int = obj["Rpt2DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3DepGainLoss:int = obj["Rpt3DepGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.LastChrgCalcDate:str = obj["LastChrgCalcDate"]
      """  The last date finance/late charges have been calculated for this invoice.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.TotFinChrg:int = obj["TotFinChrg"]
      """  Total Finance Charge amount.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.PayDiscDays:str = obj["PayDiscDays"]
      """  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  """  
      self.PayDiscPer:str = obj["PayDiscPer"]
      """  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  """  
      self.BlockedFinChrg:bool = obj["BlockedFinChrg"]
      """  Blocks certain invoice from generating finance/later charge.  """  
      self.BlockedFinChrgReason:str = obj["BlockedFinChrgReason"]
      """  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.BlockedRemLetters:bool = obj["BlockedRemLetters"]
      """  Blocks certain invoice from being printed on reminder letters.  """  
      self.PayDiscPartPay:bool = obj["PayDiscPartPay"]
      """  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  """  
      self.BlockedRemLettersReason:str = obj["BlockedRemLettersReason"]
      """  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.CurrRateDate:str = obj["CurrRateDate"]
      """  Currency Rate Date  """  
      self.PIPayment:str = obj["PIPayment"]
      """   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.UseAltBillTo:bool = obj["UseAltBillTo"]
      """  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code  """  
      self.LockTaxRate:bool = obj["LockTaxRate"]
      """  Locks Tax Rate and allows user to edit the tax exchange rate  """  
      self.SEBankRef:str = obj["SEBankRef"]
      """  Sweden Finland Localization field - Banking Reference  """  
      self.GUITaxTypeCode:str = obj["GUITaxTypeCode"]
      """  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  """  
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      """  Government Uniform Invoice Format Code (Taiwan Localization field)  """  
      self.GUIDeductCode:str = obj["GUIDeductCode"]
      """  Government Uniform Invoice Deduct Code (Taiwan Localization field)  """  
      self.ReversalDocAmount:int = obj["ReversalDocAmount"]
      """  Reversal Doucment Amount  """  
      self.OrigDueDate:str = obj["OrigDueDate"]
      """  Original Due Date at posting time  """  
      self.HeadNum:int = obj["HeadNum"]
      """  The reference to CashHead.HeadNum.Used in deposit invoices  """  
      self.ARLOCID:str = obj["ARLOCID"]
      """  Letter of Credit ID.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  The free text field which can contain reference (such as Contract)  """  
      self.OurBank:str = obj["OurBank"]
      """  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  """  
      self.ContractDate:str = obj["ContractDate"]
      """  Addition to Contract  """  
      self.PBProjectID:str = obj["PBProjectID"]
      """  If the invoice was generated in Project Billing then it is reference to the project.  """  
      self.DepositAmt:int = obj["DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment  """  
      self.GUIExportBillNumber:str = obj["GUIExportBillNumber"]
      """   Taiwan Localization
Export Bill Number  """  
      self.DocDepositAmt:int = obj["DocDepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in document currency  """  
      self.GUIDateOfExport:str = obj["GUIDateOfExport"]
      """   Taiwan Localization
Date of Export  """  
      self.Rpt1DepositAmt:int = obj["Rpt1DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt1 currency  """  
      self.GUIExportType:str = obj["GUIExportType"]
      """   Taiwan Localization
Export Type  """  
      self.Rpt2DepositAmt:int = obj["Rpt2DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt2 currency  """  
      self.GUIExportMark:str = obj["GUIExportMark"]
      """   Taiwan Localization
Export Mark  """  
      self.Rpt3DepositAmt:int = obj["Rpt3DepositAmt"]
      """  Deposit amount is transaction amount of deposit payment in Rpt23currency  """  
      self.GUIExportBillType:str = obj["GUIExportBillType"]
      """   Taiwan Localization
Export Bill Type  """  
      self.DepUnallocatedAmt:int = obj["DepUnallocatedAmt"]
      """  Deposit unallocated amount in base currency  """  
      self.SummarizationDate:str = obj["SummarizationDate"]
      """  Day when a company sums up accounts receivables for each customer.  """  
      self.DocDepUnallocatedAmt:int = obj["DocDepUnallocatedAmt"]
      """  Deposit unallocated amount in document currency  """  
      self.BillingDate:str = obj["BillingDate"]
      """  Date when a company bills the customer  """  
      self.Rpt1DepUnallocatedAmt:int = obj["Rpt1DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt1 currency  """  
      self.BillingNumber:str = obj["BillingNumber"]
      """  Billing Number to be generated from Legal Numbering upon printing of billing statement.  """  
      self.Rpt2DepUnallocatedAmt:int = obj["Rpt2DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt2 currency  """  
      self.ReadyToBill:bool = obj["ReadyToBill"]
      """  Only records ready to bill will be printed in the Billing Statement  """  
      self.Rpt3DepUnallocatedAmt:int = obj["Rpt3DepUnallocatedAmt"]
      """  Deposit unallocated amount in Rpt3 currency  """  
      self.OvrDefTaxDate:bool = obj["OvrDefTaxDate"]
      """  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  """  
      self.XRefContractNum:str = obj["XRefContractNum"]
      """  Cross Reference Contract Number.  """  
      self.XRefContractDate:str = obj["XRefContractDate"]
      """  Cross Reference Contract Date.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.CustAgentName:str = obj["CustAgentName"]
      """  Customer Agent Name  """  
      self.CustAgentTaxRegNo:str = obj["CustAgentTaxRegNo"]
      """  Customer Agent Tax Region Number  """  
      self.ExportType:str = obj["ExportType"]
      """  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  """  
      self.ExportReportNo:str = obj["ExportReportNo"]
      """  Export Report Number  """  
      self.RealEstateNo:str = obj["RealEstateNo"]
      """  Real Estate Number  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.CycleCode:str = obj["CycleCode"]
      """  CycleCode  """  
      self.Duration:int = obj["Duration"]
      """  Duration  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.MaxValueAmt:int = obj["MaxValueAmt"]
      """  MaxValueAmt  """  
      self.DocMaxValueAmt:int = obj["DocMaxValueAmt"]
      """  DocMaxValueAmt  """  
      self.Rpt1MaxValueAmt:int = obj["Rpt1MaxValueAmt"]
      """  Rpt1MaxValueAmt  """  
      self.Rpt2MaxValueAmt:int = obj["Rpt2MaxValueAmt"]
      """  Rpt2MaxValueAmt  """  
      self.Rpt3MaxValueAmt:int = obj["Rpt3MaxValueAmt"]
      """  Rpt3MaxValueAmt  """  
      self.HoldInvoice:bool = obj["HoldInvoice"]
      """  HoldInvoice  """  
      self.CopyLatestInvoice:bool = obj["CopyLatestInvoice"]
      """  CopyLatestInvoice  """  
      self.OverrideEndDate:bool = obj["OverrideEndDate"]
      """  OverrideEndDate  """  
      self.CycleInactive:bool = obj["CycleInactive"]
      """  CycleInactive  """  
      self.RecurSource:bool = obj["RecurSource"]
      """  RecurSource  """  
      self.InstanceNum:int = obj["InstanceNum"]
      """  InstanceNum  """  
      self.RecurBalance:int = obj["RecurBalance"]
      """  RecurBalance  """  
      self.DocRecurBalance:int = obj["DocRecurBalance"]
      """  DocRecurBalance  """  
      self.Rpt1RecurBalance:int = obj["Rpt1RecurBalance"]
      """  Rpt1RecurBalance  """  
      self.Rpt2RecurBalance:int = obj["Rpt2RecurBalance"]
      """  Rpt2RecurBalance  """  
      self.Rpt3RecurBalance:int = obj["Rpt3RecurBalance"]
      """  Rpt3RecurBalance  """  
      self.LastDate:str = obj["LastDate"]
      """  LastDate  """  
      self.RecurringState:str = obj["RecurringState"]
      """  RecurringState  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.InvoiceNumList:str = obj["InvoiceNumList"]
      """  InvoiceNumList  """  
      self.IsAddedToGTI:bool = obj["IsAddedToGTI"]
      """  IsAddedToGTI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CMReason:str = obj["CMReason"]
      """  CMReason  """  
      self.THIsImmatAdjustment:bool = obj["THIsImmatAdjustment"]
      """  THIsImmatAdjustment  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.RevisionDate:str = obj["RevisionDate"]
      """  RevisionDate  """  
      self.RevisionNum:int = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TWDeclareYear:int = obj["TWDeclareYear"]
      """  TWDeclareYear  """  
      self.TWDeclarePeriod:int = obj["TWDeclarePeriod"]
      """  TWDeclarePeriod  """  
      self.TWGenerationType:str = obj["TWGenerationType"]
      """  TWGenerationType  """  
      self.TWGUIGroup:str = obj["TWGUIGroup"]
      """  TWGUIGroup  """  
      self.TWPeriodPrefix:str = obj["TWPeriodPrefix"]
      """  TWPeriodPrefix  """  
      self.InvInCollections:bool = obj["InvInCollections"]
      """  Indicates if the Invoice is in Collections status  """  
      self.CollectionsCust:bool = obj["CollectionsCust"]
      """   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  """  
      self.CounterARForm:int = obj["CounterARForm"]
      """  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  """  
      self.PostedRecog:bool = obj["PostedRecog"]
      """  flag indicates if Revenue of the invoice has been already posted  """  
      self.CNConfirmDate:str = obj["CNConfirmDate"]
      """  Confirmation Date  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  MXSATSeal  """  
      self.MXSerie:str = obj["MXSerie"]
      """  MXSerie  """  
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  MXTaxRcptType  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXTotalPayments:int = obj["MXTotalPayments"]
      """  MXTotalPayments  """  
      self.MXFolio:str = obj["MXFolio"]
      """  MXFolio  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  MXCertifiedTimestamp  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  MXSATCertificateSN  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  MXDigitalSeal  """  
      self.MXPostedTimeStamp:str = obj["MXPostedTimeStamp"]
      """  MXPostedTimeStamp  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  MXCertificate  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  MXApprovalYear  """  
      self.MXCBB:str = obj["MXCBB"]
      """  MXCBB  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  MXApprovalNum  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  MXOriginalStringTFD  """  
      self.MXPaymentNum:int = obj["MXPaymentNum"]
      """  MXPaymentNum  """  
      self.MXPaidAs:str = obj["MXPaidAs"]
      """  MXPaidAs  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  MXCertificateSN  """  
      self.MXOriginalAmount:int = obj["MXOriginalAmount"]
      """  MXOriginalAmount  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.MXOriginalDate:str = obj["MXOriginalDate"]
      """  MXOriginalDate  """  
      self.MXOriginalSeries:str = obj["MXOriginalSeries"]
      """  MXOriginalSeries  """  
      self.MXOriginalFolio:str = obj["MXOriginalFolio"]
      """  MXOriginalFolio  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  MXOriginalString  """  
      self.MXPaymentName:str = obj["MXPaymentName"]
      """  MXPaymentName  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EInvStatus:int = obj["EInvStatus"]
      """  EInvStatus  """  
      self.EInvTimestamp:str = obj["EInvTimestamp"]
      """  EInvTimestamp  """  
      self.EInvUpdatedBy:str = obj["EInvUpdatedBy"]
      """  EInvUpdatedBy  """  
      self.EInvException:str = obj["EInvException"]
      """  EInvException  """  
      self.WithTaxConfirm:bool = obj["WithTaxConfirm"]
      """  Flagged that this invoice has taxes which were necessary or is necessary now.  """  
      self.UseAltBillToID:bool = obj["UseAltBillToID"]
      """  UseAltBillToID  """  
      self.MXCancelledDate:str = obj["MXCancelledDate"]
      """  MXCancelledDate  """  
      self.Overpaid:bool = obj["Overpaid"]
      """  Overpaid  """  
      self.OrdExchangeRate:int = obj["OrdExchangeRate"]
      """  OrdExchangeRate  """  
      self.PEAPPayNum:int = obj["PEAPPayNum"]
      """  PEAPPayNum  """  
      self.PEBankNumber:str = obj["PEBankNumber"]
      """  PEBankNumber  """  
      self.PECharges:int = obj["PECharges"]
      """  PECharges  """  
      self.PECommissions:int = obj["PECommissions"]
      """  PECommissions  """  
      self.PEDetTaxAmt:int = obj["PEDetTaxAmt"]
      """  PEDetTaxAmt  """  
      self.PEDetTaxCurrencyCode:str = obj["PEDetTaxCurrencyCode"]
      """  PEDetTaxCurrencyCode  """  
      self.PEDischargeAmt:int = obj["PEDischargeAmt"]
      """  PEDischargeAmt  """  
      self.PEDischargeDate:str = obj["PEDischargeDate"]
      """  PEDischargeDate  """  
      self.PEInterest:int = obj["PEInterest"]
      """  PEInterest  """  
      self.PENoPayPenalty:int = obj["PENoPayPenalty"]
      """  PENoPayPenalty  """  
      self.PESUNATDepAmt:int = obj["PESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.PESUNATDepDate:str = obj["PESUNATDepDate"]
      """  CSF Peru - SUNAT Deposit Date  """  
      self.PESUNATDepNum:str = obj["PESUNATDepNum"]
      """  CSF Peru -  SUNAT Deposit Number  """  
      self.PEBOEPosted:bool = obj["PEBOEPosted"]
      """  PEBOEPosted  """  
      self.DocPEInterest:int = obj["DocPEInterest"]
      """  DocPEInterest  """  
      self.DocPECommissions:int = obj["DocPECommissions"]
      """  DocPECommissions  """  
      self.DocPECharges:int = obj["DocPECharges"]
      """  DocPECharges  """  
      self.DocPENoPayPenalty:int = obj["DocPENoPayPenalty"]
      """  DocPENoPayPenalty  """  
      self.DocPEDischargeAmt:int = obj["DocPEDischargeAmt"]
      """  DocPEDischargeAmt  """  
      self.DocPEDetTaxAmt:int = obj["DocPEDetTaxAmt"]
      """  DocPEDetTaxAmt  """  
      self.Rpt1PEInterest:int = obj["Rpt1PEInterest"]
      """  Rpt1PEInterest  """  
      self.Rpt1PECommissions:int = obj["Rpt1PECommissions"]
      """  Rpt1PECommissions  """  
      self.Rpt1PECharges:int = obj["Rpt1PECharges"]
      """  Rpt1PECharges  """  
      self.Rpt1PENoPayPenalty:int = obj["Rpt1PENoPayPenalty"]
      """  Rpt1PENoPayPenalty  """  
      self.Rpt1PEDischargeAmt:int = obj["Rpt1PEDischargeAmt"]
      """  Rpt1PEDischargeAmt  """  
      self.Rpt2PEInterest:int = obj["Rpt2PEInterest"]
      """  Rpt2PEInterest  """  
      self.Rpt2PECommissions:int = obj["Rpt2PECommissions"]
      """  Rpt2PECommissions  """  
      self.Rpt2PECharges:int = obj["Rpt2PECharges"]
      """  Rpt2PECharges  """  
      self.Rpt2PENoPayPenalty:int = obj["Rpt2PENoPayPenalty"]
      """  Rpt2PENoPayPenalty  """  
      self.Rpt2PEDischargeAmt:int = obj["Rpt2PEDischargeAmt"]
      """  Rpt2PEDischargeAmt  """  
      self.Rpt3PEInterest:int = obj["Rpt3PEInterest"]
      """  Rpt3PEInterest  """  
      self.Rpt3PECommissions:int = obj["Rpt3PECommissions"]
      """  Rpt3PECommissions  """  
      self.Rpt3PECharges:int = obj["Rpt3PECharges"]
      """  Rpt3PECharges  """  
      self.Rpt3PENoPayPenalty:int = obj["Rpt3PENoPayPenalty"]
      """  Rpt3PENoPayPenalty  """  
      self.Rpt3PEDischargeAmt:int = obj["Rpt3PEDischargeAmt"]
      """  Rpt3PEDischargeAmt  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Supplier Code  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEBOEStatus:str = obj["PEBOEStatus"]
      """  PEBOEStatus  """  
      self.PEBOEIsMultiGen:bool = obj["PEBOEIsMultiGen"]
      """  PEBOEIsMultiGen  """  
      self.PERefDocID:str = obj["PERefDocID"]
      """  PE Reference Document ID  """  
      self.PEReasonCode:str = obj["PEReasonCode"]
      """  PE Reason Code  """  
      self.PEReasonDesc:str = obj["PEReasonDesc"]
      """  PE Reason Description  """  
      self.TWGUIRegNumSeller:str = obj["TWGUIRegNumSeller"]
      """  TW GUI Code Seller  """  
      self.TWGUIRegNumBuyer:str = obj["TWGUIRegNumBuyer"]
      """  TW GUI Code Buyer  """  
      self.TWGUIExportDocumentName:str = obj["TWGUIExportDocumentName"]
      """  Document Name  """  
      self.TWGUIExportRemarks:str = obj["TWGUIExportRemarks"]
      """  Remarks  """  
      self.TWGUIExportVerification:str = obj["TWGUIExportVerification"]
      """  Verification  """  
      self.PEDebitNoteReasonCode:str = obj["PEDebitNoteReasonCode"]
      """  PEDebitNoteReasonCode  """  
      self.PEDebitNote:bool = obj["PEDebitNote"]
      """  PEDebitNote  """  
      self.MXPartPmt:bool = obj["MXPartPmt"]
      """  MXPartPmt  """  
      self.CNTaxInvoiceType:int = obj["CNTaxInvoiceType"]
      """  Tax Invoice Type  """  
      self.MXExportOperationType:str = obj["MXExportOperationType"]
      """  MXExportOperationType  """  
      self.MXExportCustDocCode:str = obj["MXExportCustDocCode"]
      """  MXExportCustDocCode  """  
      self.MXExportCertOriginNum:str = obj["MXExportCertOriginNum"]
      """  MXExportCertOriginNum  """  
      self.MXExportConfNum:str = obj["MXExportConfNum"]
      """  MXExportConfNum  """  
      self.MXExportCertOrigin:bool = obj["MXExportCertOrigin"]
      """  MXExportCertOrigin  """  
      self.MXIncoterm:str = obj["MXIncoterm"]
      """  MXIncoterm  """  
      self.AGDocConcept:int = obj["AGDocConcept"]
      """  AGDocConcept  """  
      self.EInvRefNum:str = obj["EInvRefNum"]
      """  Electronic Invoice reference number  """  
      self.ExportDocRefNum:str = obj["ExportDocRefNum"]
      """  Export document reference number  """  
      self.ExportDocDate:str = obj["ExportDocDate"]
      """  Export document date  """  
      self.INTaxTransactionID:str = obj["INTaxTransactionID"]
      """  Tax Transaction ID  """  
      self.MXMovingReasonFlag:bool = obj["MXMovingReasonFlag"]
      """  MXMovingReasonFlag  """  
      self.MXMovingReason:str = obj["MXMovingReason"]
      """  MXMovingReason  """  
      self.MXNumRegIdTrib:str = obj["MXNumRegIdTrib"]
      """  MXNumRegIdTrib  """  
      self.MXResidenCountryNum:int = obj["MXResidenCountryNum"]
      """  MXResidenCountryNum  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.MXConfirmationCode:str = obj["MXConfirmationCode"]
      """  MXConfirmationCode  """  
      self.MXExternalCode:str = obj["MXExternalCode"]
      """  MXExternalCode  """  
      self.ServiceInvoice:bool = obj["ServiceInvoice"]
      """  This invoice was created via an integration with a third-party field service.  """  
      self.MXDomesticTransfer:bool = obj["MXDomesticTransfer"]
      """  MXDomesticTransfer  """  
      self.MXCancellationMode:str = obj["MXCancellationMode"]
      """  MXCancellationMode  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      """  Shipping Port Code  """  
      self.INExportProcedure:str = obj["INExportProcedure"]
      """  Export Procedure  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.DepositBalance:int = obj["DepositBalance"]
      """  DepositBalance  """  
      self.DocDepositBalance:int = obj["DocDepositBalance"]
      """  DocDepositBalance  """  
      self.Rpt1DepositBalance:int = obj["Rpt1DepositBalance"]
      """  Rpt1DepositBalance  """  
      self.Rpt2DepositBalance:int = obj["Rpt2DepositBalance"]
      """  Rpt2DepositBalance  """  
      self.Rpt3DepositBalance:int = obj["Rpt3DepositBalance"]
      """  Rpt3DepositBalance  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this invoice record is associated with.  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case related to this invoice.  """  
      self.CreditOverride:bool = obj["CreditOverride"]
      """  Indicates that the credit hold was overridden for this invoice.  """  
      self.CreditOverrideDate:str = obj["CreditOverrideDate"]
      """  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  """  
      self.CreditOverrideUserID:str = obj["CreditOverrideUserID"]
      """  The user id that override the invoice credit hold.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  """  
      self.PEXMLType:int = obj["PEXMLType"]
      """  Peru Electronic Invoice XML Type  """  
      self.COCreditMemoReasonCode:str = obj["COCreditMemoReasonCode"]
      """  COCreditMemoReasonCode  """  
      self.CODebitMemoReasonCode:str = obj["CODebitMemoReasonCode"]
      """  CODebitMemoReasonCode  """  
      self.COReasonDesc:str = obj["COReasonDesc"]
      """  COReasonDesc  """  
      self.CODebitNote:bool = obj["CODebitNote"]
      """  CODebitNote  """  
      self.PEDetractionTranNum:int = obj["PEDetractionTranNum"]
      """  PEDetractionTranNum  """  
      self.PEProductCode:str = obj["PEProductCode"]
      """  PEProductCode  """  
      self.PECollectionGroupID:str = obj["PECollectionGroupID"]
      """  PECollectionGroupID  """  
      self.PECaptionCode:str = obj["PECaptionCode"]
      """  PE Caption Code  """  
      self.PECaption:str = obj["PECaption"]
      """  PE Caption Code Description  """  
      self.PERefDocumentType:str = obj["PERefDocumentType"]
      """  PE Reference DocumentType 1  """  
      self.PERefDocumentNumber:str = obj["PERefDocumentNumber"]
      """  PE Reference Document Number 1  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PERefDocumentType2:str = obj["PERefDocumentType2"]
      """  PE Reference DocumentType 2  """  
      self.PERefDocumentType3:str = obj["PERefDocumentType3"]
      """  PE Reference DocumentType 3  """  
      self.PERefDocumentType4:str = obj["PERefDocumentType4"]
      """  PE Reference DocumentType 4  """  
      self.PERefDocumentType5:str = obj["PERefDocumentType5"]
      """  PE Reference DocumentType 5  """  
      self.PERefDocumentNumber2:str = obj["PERefDocumentNumber2"]
      """  PE Reference Document Number 2  """  
      self.PERefDocumentNumber3:str = obj["PERefDocumentNumber3"]
      """  PE Reference Document Number 3  """  
      self.PERefDocumentNumber4:str = obj["PERefDocumentNumber4"]
      """  PE Reference Document Number 4  """  
      self.PERefDocumentNumber5:str = obj["PERefDocumentNumber5"]
      """  PE Reference Document Number 5  """  
      self.ELIEInvoice:bool = obj["ELIEInvoice"]
      """  E-invoice  """  
      self.ELIEInvStatus:int = obj["ELIEInvStatus"]
      """  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  """  
      self.ELIEInvUpdatedBy:str = obj["ELIEInvUpdatedBy"]
      """  User Id of the person generated E-invoice.  """  
      self.ELIEInvException:str = obj["ELIEInvException"]
      """  E-invoice error description.  """  
      self.ELIEInvUpdatedOn:str = obj["ELIEInvUpdatedOn"]
      """  Date and Time of E-invoice generation.  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Flag that indicates if the Invoice is for Central Collection.  """  
      self.CColChildCompany:str = obj["CColChildCompany"]
      """  Company that created this invoice.  """  
      self.CColParentCompany:str = obj["CColParentCompany"]
      """  Central Collection company.  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the invoicing company.  """  
      self.CColChildInvoiceNum:int = obj["CColChildInvoiceNum"]
      """  Invoice number on the invoicing company.  """  
      self.CColInvoiceNum:int = obj["CColInvoiceNum"]
      """  Invoice number on central collection company  """  
      self.CColChildLegalNumber:str = obj["CColChildLegalNumber"]
      """  Legal number on the invoicing company invoice.  """  
      self.CColLegalNumber:str = obj["CColLegalNumber"]
      """  Legal number on central collection company.  """  
      self.CColInvoiceRef:int = obj["CColInvoiceRef"]
      """  Invoice reference on the Invoicing Company.  """  
      self.CColInvBal:int = obj["CColInvBal"]
      """  Invoice Balance in the Central Collection company.  """  
      self.DocCColInvBal:int = obj["DocCColInvBal"]
      """  Central Collection Doc Invoice Balance.  """  
      self.CColInvAmt:int = obj["CColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.DocCColInvAmt:int = obj["DocCColInvAmt"]
      """  Invoice Amount on the Invoicing Company.  """  
      self.Rpt1CColInvBal:int = obj["Rpt1CColInvBal"]
      """  Rpt 1 Parent Invoice Balance  """  
      self.Rpt2CColInvBal:int = obj["Rpt2CColInvBal"]
      """  Rpt 2 Parent Invoice Balance  """  
      self.Rpt3CColInvBal:int = obj["Rpt3CColInvBal"]
      """  Rpt 3 Parent Invoice Balance  """  
      self.Rpt1CColInvAmt:int = obj["Rpt1CColInvAmt"]
      """  Rpt 1 Child Invoice Amount  """  
      self.Rpt2CColInvAmt:int = obj["Rpt2CColInvAmt"]
      """  Rpt 2 Child Invoice Amount  """  
      self.Rpt3CColInvAmt:int = obj["Rpt3CColInvAmt"]
      """  Rpt 3 Child Invoice Amount  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.ELIEInvTerminalName:str = obj["ELIEInvTerminalName"]
      """  User terminal name  """  
      self.ELIEInvTerminalIP:str = obj["ELIEInvTerminalIP"]
      """  User terminal IP  """  
      self.Description:str = obj["Description"]
      """  GL Description  """  
      self.WithholdAcctToInterim:bool = obj["WithholdAcctToInterim"]
      """  WithholdAcctToInterim  """  
      self.CColOpenInvoice:bool = obj["CColOpenInvoice"]
      """  Indicates if the Central Collection parent invoice is open.  """  
      self.AGQRCodeData:str = obj["AGQRCodeData"]
      """  AGQRCodeData  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.ELIEInvID:str = obj["ELIEInvID"]
      """  EInvoice ID  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallLine:int = obj["CallLine"]
      """  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.MXCancelReasonCode:str = obj["MXCancelReasonCode"]
      """  MXCancelReasonCode  """  
      self.MXSubstInvoiceNum:int = obj["MXSubstInvoiceNum"]
      """  MXSubstInvoiceNum  """  
      self.MXExportType:str = obj["MXExportType"]
      """  MXExportType  """  
      self.MXGlobalInvoicePeriod:str = obj["MXGlobalInvoicePeriod"]
      """  MXGlobalInvoicePeriod  """  
      self.MXGlobalInvoiceMonth:str = obj["MXGlobalInvoiceMonth"]
      """  MXGlobalInvoiceMonth  """  
      self.ELIEInvServiceProviderStatus:int = obj["ELIEInvServiceProviderStatus"]
      """  ELIEInvServiceProviderStatus  """  
      self.IncotermCode:str = obj["IncotermCode"]
      """  Incoterm Code  """  
      self.IncotermLocation:str = obj["IncotermLocation"]
      """  Incoterm Location  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.ABAmt:int = obj["ABAmt"]
      """  Total advanced billing amount.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.ARPNHeadNum:int = obj["ARPNHeadNum"]
      """  ARPNHead's HeadNum  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  """  
      self.AutoGenPN:bool = obj["AutoGenPN"]
      """  Auto generate payment instruments  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers.  """  
      self.BankForPI:str = obj["BankForPI"]
      """  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  """  
      self.BankForPIName:str = obj["BankForPIName"]
      self.BTCustID:str = obj["BTCustID"]
      """  Customer ID for the bill to customer (InvcHead.CustNum).  """  
      self.BTCustomerName:str = obj["BTCustomerName"]
      """  Bill to customer name.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CNGTIAction:str = obj["CNGTIAction"]
      self.CNGTIAddress:str = obj["CNGTIAddress"]
      self.CNGTIBankAccount:str = obj["CNGTIBankAccount"]
      self.CNGTIComment:str = obj["CNGTIComment"]
      self.CNGTICustomerName:str = obj["CNGTICustomerName"]
      self.CNGTIExportAddress:str = obj["CNGTIExportAddress"]
      self.CNGTIGrossInvcAmt:int = obj["CNGTIGrossInvcAmt"]
      """  CSF China, Gross Invoice Amount  """  
      self.CNGTIInvoiceAmt:int = obj["CNGTIInvoiceAmt"]
      """  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  """  
      self.CNGTINote:str = obj["CNGTINote"]
      self.CNGTIShipToNum:str = obj["CNGTIShipToNum"]
      self.CNGTIStatus1:str = obj["CNGTIStatus1"]
      self.CNGTIStatus2:bool = obj["CNGTIStatus2"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.COIFRSCalculation:bool = obj["COIFRSCalculation"]
      """  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  """  
      self.COIFRSEnabled:bool = obj["COIFRSEnabled"]
      """  If true then Colombia IFRS Net Present Value calculation is enabled  """  
      self.COIFRSFinancialCharge:int = obj["COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.COIFRSInterestRate:int = obj["COIFRSInterestRate"]
      self.COIFRSNumberOfPeriods:int = obj["COIFRSNumberOfPeriods"]
      """  Number of Periods for payment  """  
      self.COIFRSPresentValue:int = obj["COIFRSPresentValue"]
      """  Present Value  """  
      self.CollectionsInv:bool = obj["CollectionsInv"]
      """  Indicates if Invoice is in Collections (Peru localization)  """  
      self.ContactEmailAddr:str = obj["ContactEmailAddr"]
      """  Contact email address.  """  
      self.ContactFaxNum:str = obj["ContactFaxNum"]
      """  Contact fax number  """  
      self.ContactName:str = obj["ContactName"]
      """  Contact name  """  
      self.ContactPhoneNum:str = obj["ContactPhoneNum"]
      """  Contact phone number  """  
      self.ConvertedFromDep:bool = obj["ConvertedFromDep"]
      """  record converted from deposit  """  
      self.COOperTypeDesc:str = obj["COOperTypeDesc"]
      self.CountryIntrastat:bool = obj["CountryIntrastat"]
      """  True if the Country set for the current company contains an Intrastat code.  """  
      self.CumulativeBalance:int = obj["CumulativeBalance"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CurrentInstanceNum:int = obj["CurrentInstanceNum"]
      self.CustAllowOTS:bool = obj["CustAllowOTS"]
      self.CustOnCreditHold:bool = obj["CustOnCreditHold"]
      self.DepBal:int = obj["DepBal"]
      """  Deposit balance from CashHed  """  
      self.DepositCreditEnabled:bool = obj["DepositCreditEnabled"]
      """  Deposit credit enabled flag.  """  
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.DisableAplDate:bool = obj["DisableAplDate"]
      """  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  """  
      self.DispBalDN:int = obj["DispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DisplayBillAddr:str = obj["DisplayBillAddr"]
      """  Bill to address in list format.  """  
      self.DisplayCreditCardNum:str = obj["DisplayCreditCardNum"]
      """  Display field for the masked credit card number  """  
      self.DisplayCurrencyID:str = obj["DisplayCurrencyID"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DNPmtAmt:int = obj["DNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.DocABAmt:int = obj["DocABAmt"]
      """  Document Total advanced billing amount.  """  
      self.DocCOIFRSFinancialCharge:int = obj["DocCOIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.DocCOIFRSPresentValue:int = obj["DocCOIFRSPresentValue"]
      """  Present Value  """  
      self.DocCumulativeBalance:int = obj["DocCumulativeBalance"]
      self.DocDepBal:int = obj["DocDepBal"]
      """  Document deposit amount from cashhead.  """  
      self.DocDispBalDN:int = obj["DocDispBalDN"]
      """  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol  """  
      self.DocDNPmtAmt:int = obj["DocDNPmtAmt"]
      """  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  """  
      self.DocDspPrepDeposit:int = obj["DocDspPrepDeposit"]
      self.DocDspTaxAmt:int = obj["DocDspTaxAmt"]
      self.DocPESUNATDepAmt:int = obj["DocPESUNATDepAmt"]
      """  CSF Peru - SUNAT Deposit Amount  """  
      self.DocRemainTaxAmt:int = obj["DocRemainTaxAmt"]
      self.DocReverseTaxAmt:int = obj["DocReverseTaxAmt"]
      self.DocSATaxAmt:int = obj["DocSATaxAmt"]
      self.DocSourceRecurBalance:int = obj["DocSourceRecurBalance"]
      self.DocSubTotal:int = obj["DocSubTotal"]
      """  Document sub total  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Document Total tax amount from InvcTax for Collection type 'Invoice'  """  
      self.DocVr:int = obj["DocVr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  """  
      self.DocWHTaxAmt:int = obj["DocWHTaxAmt"]
      self.DspABAmt:int = obj["DspABAmt"]
      """  Display advance billing amount  """  
      self.DspDepBal:int = obj["DspDepBal"]
      """  Display deposit balance.  """  
      self.DspDepCr:int = obj["DspDepCr"]
      """  Display deposit credit.  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.DspDocABAmt:int = obj["DspDocABAmt"]
      """  Display document advance billing amount  """  
      self.DspDocDepBal:int = obj["DspDocDepBal"]
      """  Display document deposit balance  """  
      self.DspDocDepCr:int = obj["DspDocDepCr"]
      """  Display document deposit credit.  """  
      self.DspDocInvoiceAmt:int = obj["DspDocInvoiceAmt"]
      """  Display document invoice amount  """  
      self.DspDocInvoiceBal:int = obj["DspDocInvoiceBal"]
      """  Display document invoice balance  """  
      self.DspDocRounding:int = obj["DspDocRounding"]
      """  Display Invoice Doc Rounding  """  
      self.DspDocSubTotal:int = obj["DspDocSubTotal"]
      """  display document sub total  """  
      self.DspInvoiceAmt:int = obj["DspInvoiceAmt"]
      """  Display invoice amount  """  
      self.DspInvoiceBal:int = obj["DspInvoiceBal"]
      """  Display Invoice Balance.  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display invoice reference  """  
      self.DspPayDiscDays:str = obj["DspPayDiscDays"]
      self.DspPrepDeposit:int = obj["DspPrepDeposit"]
      self.DspRounding:int = obj["DspRounding"]
      """  Display Rounding in Base  """  
      self.dspSoldToCustID:str = obj["dspSoldToCustID"]
      """  If SoldTo and Alt-Bill to are the same, this displays as null.  """  
      self.DspSubTotal:int = obj["DspSubTotal"]
      """  Display sub total  """  
      self.DspTaxAmt:int = obj["DspTaxAmt"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableCentralCollection:bool = obj["EnableCentralCollection"]
      self.EnableSOCCDefaults:bool = obj["EnableSOCCDefaults"]
      """  Flag to determine if UseSOCCDefaults should be enabled.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.ERSInvoice:bool = obj["ERSInvoice"]
      """  It will be displayed to identify invoices automatically generated due ERS shipments.  """  
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  """  
      self.GenedFromRMA:bool = obj["GenedFromRMA"]
      """  Flag for update of InvcHead to allow when group id is "RMACRREQ"  """  
      self.HasBank:bool = obj["HasBank"]
      """  CustBank record exists for customer  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for ar invoices/credit memos  """  
      self.InPriceLn:bool = obj["InPriceLn"]
      """  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  """  
      self.IntInvoiceType:str = obj["IntInvoiceType"]
      """  Integration invoice type.  Used for setting of InvoiceType.  """  
      self.InvoiceTypeDesc:str = obj["InvoiceTypeDesc"]
      """  InvoiceType description  """  
      self.IsDK:bool = obj["IsDK"]
      """  Denmark localization external field  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsLatestRecurrence:bool = obj["IsLatestRecurrence"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.IsPIUnappliedReceipt:bool = obj["IsPIUnappliedReceipt"]
      """  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  """  
      self.IsPMForGenPIType:bool = obj["IsPMForGenPIType"]
      self.LatestInvoice:int = obj["LatestInvoice"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  Stores the message when a legal number is generated.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.MXCancellationID:str = obj["MXCancellationID"]
      """  MXCancellationID  """  
      self.MXCancellationStatus:str = obj["MXCancellationStatus"]
      """  MXCancellationStatus  """  
      self.NeedConfirmTaxes:bool = obj["NeedConfirmTaxes"]
      """  It indicates that this Invoice has taxes, for which the confirmation is required.  """  
      self.NextDiscDate:str = obj["NextDiscDate"]
      """  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  """  
      self.NextInvoiceDate:str = obj["NextInvoiceDate"]
      """  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  """  
      self.PackSlipNum:int = obj["PackSlipNum"]
      """  Pack slip number from the 1st line item.  """  
      self.PaySchedEnabled:bool = obj["PaySchedEnabled"]
      """  Pay schedule enabled flag  """  
      self.PEBOEChangeStatusTo:str = obj["PEBOEChangeStatusTo"]
      """  Indicates what the user will change the status to  """  
      self.PEBOEStatusDesc:str = obj["PEBOEStatusDesc"]
      self.PECollectionsDate:str = obj["PECollectionsDate"]
      """  Peru CSF: Collections date  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEInCollections:bool = obj["PEInCollections"]
      """  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  """  
      self.PERefDocumentTypeDesc:str = obj["PERefDocumentTypeDesc"]
      """  PE Document Type Description  """  
      self.PERefDocumentTypeDesc2:str = obj["PERefDocumentTypeDesc2"]
      """  PE Document Type Description 2  """  
      self.PERefDocumentTypeDesc3:str = obj["PERefDocumentTypeDesc3"]
      """  PE Document Type Description 3  """  
      self.PERefDocumentTypeDesc4:str = obj["PERefDocumentTypeDesc4"]
      """  PE Document Type Description 4  """  
      self.PERefDocumentTypeDesc5:str = obj["PERefDocumentTypeDesc5"]
      """  PE Document Type Description 5  """  
      self.PIBankAcctID:str = obj["PIBankAcctID"]
      """  PI - Bank account  """  
      self.PICustBankDtl:bool = obj["PICustBankDtl"]
      """  PI Customer bank required  """  
      self.PIInitiation:str = obj["PIInitiation"]
      """  PI Initiation - generated or received  """  
      self.PrepDepositEnabled:bool = obj["PrepDepositEnabled"]
      """  Prep Deposit enabled flag.  """  
      self.ProposedTaxRgn:str = obj["ProposedTaxRgn"]
      """  The description of the proposed Tax Region  """  
      self.RecalcAmts:str = obj["RecalcAmts"]
      """   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  """  
      self.Recurring:bool = obj["Recurring"]
      """  Recurring flag  """  
      self.RemainTaxAmt:int = obj["RemainTaxAmt"]
      self.ReminderSeq:int = obj["ReminderSeq"]
      self.ReversalDocAmt:int = obj["ReversalDocAmt"]
      """  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  """  
      self.ReverseTaxAmt:int = obj["ReverseTaxAmt"]
      self.Rpt1ABAmt:int = obj["Rpt1ABAmt"]
      self.Rpt1COIFRSFinancialCharge:int = obj["Rpt1COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt1COIFRSPresentValue:int = obj["Rpt1COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt1CumulativeBalance:int = obj["Rpt1CumulativeBalance"]
      self.Rpt1DepBal:int = obj["Rpt1DepBal"]
      self.Rpt1DspABAmt:int = obj["Rpt1DspABAmt"]
      self.Rpt1DspDepBal:int = obj["Rpt1DspDepBal"]
      self.Rpt1DspDepCr:int = obj["Rpt1DspDepCr"]
      self.Rpt1DspInvoiceAmt:int = obj["Rpt1DspInvoiceAmt"]
      self.Rpt1DspInvoiceBal:int = obj["Rpt1DspInvoiceBal"]
      self.Rpt1DspPrepDeposit:int = obj["Rpt1DspPrepDeposit"]
      self.Rpt1DspRounding:int = obj["Rpt1DspRounding"]
      self.Rpt1DspSubTotal:int = obj["Rpt1DspSubTotal"]
      self.Rpt1DspTaxAmt:int = obj["Rpt1DspTaxAmt"]
      self.Rpt1RemainTaxAmt:int = obj["Rpt1RemainTaxAmt"]
      self.Rpt1ReverseTaxAmt:int = obj["Rpt1ReverseTaxAmt"]
      self.Rpt1SATaxAmt:int = obj["Rpt1SATaxAmt"]
      self.Rpt1SourceRecurBalance:int = obj["Rpt1SourceRecurBalance"]
      self.Rpt1SubTotal:int = obj["Rpt1SubTotal"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt1Vr:int = obj["Rpt1Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  """  
      self.Rpt1WHTaxAmt:int = obj["Rpt1WHTaxAmt"]
      self.Rpt2ABAmt:int = obj["Rpt2ABAmt"]
      self.Rpt2COIFRSFinancialCharge:int = obj["Rpt2COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt2COIFRSPresentValue:int = obj["Rpt2COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt2CumulativeBalance:int = obj["Rpt2CumulativeBalance"]
      self.Rpt2DepBal:int = obj["Rpt2DepBal"]
      self.Rpt2DspABAmt:int = obj["Rpt2DspABAmt"]
      self.Rpt2DspDepBal:int = obj["Rpt2DspDepBal"]
      self.Rpt2DspDepCr:int = obj["Rpt2DspDepCr"]
      self.Rpt2DspInvoiceAmt:int = obj["Rpt2DspInvoiceAmt"]
      self.Rpt2DspInvoiceBal:int = obj["Rpt2DspInvoiceBal"]
      self.Rpt2DspPrepDeposit:int = obj["Rpt2DspPrepDeposit"]
      self.Rpt2DspRounding:int = obj["Rpt2DspRounding"]
      self.Rpt2DspSubTotal:int = obj["Rpt2DspSubTotal"]
      self.Rpt2DspTaxAmt:int = obj["Rpt2DspTaxAmt"]
      self.Rpt2RemainTaxAmt:int = obj["Rpt2RemainTaxAmt"]
      self.Rpt2ReverseTaxAmt:int = obj["Rpt2ReverseTaxAmt"]
      self.Rpt2SATaxAmt:int = obj["Rpt2SATaxAmt"]
      self.Rpt2SourceRecurBalance:int = obj["Rpt2SourceRecurBalance"]
      self.Rpt2SubTotal:int = obj["Rpt2SubTotal"]
      self.Rpt2Taxamt:int = obj["Rpt2Taxamt"]
      self.Rpt2Vr:int = obj["Rpt2Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  """  
      self.Rpt2WHTaxAmt:int = obj["Rpt2WHTaxAmt"]
      self.Rpt3ABAmt:int = obj["Rpt3ABAmt"]
      self.Rpt3COIFRSFinancialCharge:int = obj["Rpt3COIFRSFinancialCharge"]
      """  Financial Charge  """  
      self.Rpt3COIFRSPresentValue:int = obj["Rpt3COIFRSPresentValue"]
      """  Present Value  """  
      self.Rpt3CumulativeBalance:int = obj["Rpt3CumulativeBalance"]
      self.Rpt3DepBal:int = obj["Rpt3DepBal"]
      self.Rpt3DspABAmt:int = obj["Rpt3DspABAmt"]
      self.Rpt3DspDepBal:int = obj["Rpt3DspDepBal"]
      self.Rpt3DspDepCr:int = obj["Rpt3DspDepCr"]
      self.Rpt3DspInvoiceAmt:int = obj["Rpt3DspInvoiceAmt"]
      self.Rpt3DspInvoiceBal:int = obj["Rpt3DspInvoiceBal"]
      self.Rpt3DspPrepDeposit:int = obj["Rpt3DspPrepDeposit"]
      self.Rpt3DspRounding:int = obj["Rpt3DspRounding"]
      self.Rpt3DspSubTotal:int = obj["Rpt3DspSubTotal"]
      self.Rpt3DspTaxAmt:int = obj["Rpt3DspTaxAmt"]
      self.Rpt3RemainTaxAmt:int = obj["Rpt3RemainTaxAmt"]
      self.Rpt3ReverseTaxAmt:int = obj["Rpt3ReverseTaxAmt"]
      self.Rpt3SATaxAmt:int = obj["Rpt3SATaxAmt"]
      self.Rpt3SourceRecurBalance:int = obj["Rpt3SourceRecurBalance"]
      self.Rpt3SubTotal:int = obj["Rpt3SubTotal"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.Rpt3Vr:int = obj["Rpt3Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  """  
      self.Rpt3WHTaxAmt:int = obj["Rpt3WHTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st entry in SalesRepList  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd entry in SalesRepList  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd entry in SalesRepList.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th entry in SalesRepList  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th entry in SalesRepList  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.SATaxAmt:int = obj["SATaxAmt"]
      self.Selected:bool = obj["Selected"]
      """  Boolean for selection of invoices in grid  """  
      self.SkipRecurring:bool = obj["SkipRecurring"]
      self.SoldToAddressList:str = obj["SoldToAddressList"]
      """  Sold to address list.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  Sold to customer id  """  
      self.SoldToCustomerName:str = obj["SoldToCustomerName"]
      """  Sold to customer name.  """  
      self.SourceInvoiceNum:int = obj["SourceInvoiceNum"]
      self.SourceLastDate:str = obj["SourceLastDate"]
      self.SourceRecurBalance:int = obj["SourceRecurBalance"]
      self.SubTotal:int = obj["SubTotal"]
      """  Sub total for invoice  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Total tax amount from InvcTax  """  
      self.TaxExchangeRate:int = obj["TaxExchangeRate"]
      self.TaxRgnLineChange:bool = obj["TaxRgnLineChange"]
      """  The flag to indicate if the user is supposed to be asked about Tax Liability change  """  
      self.TotalInstanceNum:int = obj["TotalInstanceNum"]
      self.TransApplyDate:str = obj["TransApplyDate"]
      """  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  """  
      self.UseSOCCDefaults:bool = obj["UseSOCCDefaults"]
      """  If true, the credit card info will come from the sales order.  """  
      self.UseTaxRate:bool = obj["UseTaxRate"]
      self.VNInvDescription:str = obj["VNInvDescription"]
      self.VNInvoiceType:str = obj["VNInvoiceType"]
      self.Vr:int = obj["Vr"]
      """  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  """  
      self.WHTaxAmt:int = obj["WHTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      """  Currency label  """  
      self.zEnableCreditHold:bool = obj["zEnableCreditHold"]
      self.AgingDays:int = obj["AgingDays"]
      """  The number of days the invoice is past due.  """  
      self.ELIEInvProhibitedStatuses:str = obj["ELIEInvProhibitedStatuses"]
      """   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  """  
      self.EnableIncotermLocation:bool = obj["EnableIncotermLocation"]
      """  Flag indicating whether to enable Incoterm Location  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.ARSystLNReqForInvc:bool = obj["ARSystLNReqForInvc"]
      self.CardTypeDescription:str = obj["CardTypeDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerMXGeneralPublic:bool = obj["CustomerMXGeneralPublic"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerELISendingOption:int = obj["CustomerELISendingOption"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.IncotermsDescription:str = obj["IncotermsDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MXPurchaseTypeCodeDesc:str = obj["MXPurchaseTypeCodeDesc"]
      self.MXSubstInvoiceMXFiscalFolio:str = obj["MXSubstInvoiceMXFiscalFolio"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OurBankPayerRef:str = obj["OurBankPayerRef"]
      self.OurBankBankIdentifier:str = obj["OurBankBankIdentifier"]
      self.OurBankTypeCode:str = obj["OurBankTypeCode"]
      self.OurBankBankAcctID:str = obj["OurBankBankAcctID"]
      self.OurBankCheckingAccount:str = obj["OurBankCheckingAccount"]
      self.OurBankBankName:str = obj["OurBankBankName"]
      self.OurBankIBANCode:str = obj["OurBankIBANCode"]
      self.OurBankLocalBIC:str = obj["OurBankLocalBIC"]
      self.OurBankDescription:str = obj["OurBankDescription"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.RecurringCycleMaximumValue:bool = obj["RecurringCycleMaximumValue"]
      self.SoldToCustNumInactive:bool = obj["SoldToCustNumInactive"]
      self.SoldToCustNumCustID:str = obj["SoldToCustNumCustID"]
      self.SoldToCustNumName:str = obj["SoldToCustNumName"]
      self.TaxRateGrpDescription:str = obj["TaxRateGrpDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.XbSystOCRCalcType:bool = obj["XbSystOCRCalcType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcHeadTableset:
   def __init__(self, obj):
      self.InvcHead:list[Erp_Tablesets_InvcHeadRow] = obj["InvcHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PEARInvSelBOTableset:
   def __init__(self, obj):
      self.PEARInvSel:list[Erp_Tablesets_PEARInvSelRow] = obj["PEARInvSel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PEARInvSelRow:
   def __init__(self, obj):
      self.Selected:bool = obj["Selected"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.DetractionTaxAmt:int = obj["DetractionTaxAmt"]
      self.LastCashReceiptDate:str = obj["LastCashReceiptDate"]
      self.ProductCode:str = obj["ProductCode"]
      self.CustID:str = obj["CustID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocDetractionTaxAmt:int = obj["DocDetractionTaxAmt"]
      self.DueDate:str = obj["DueDate"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.CustBalance:int = obj["CustBalance"]
      self.CustAmount:int = obj["CustAmount"]
      self.Balance:int = obj["Balance"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.PECollectionsDate:str = obj["PECollectionsDate"]
      self.InvInCollections:bool = obj["InvInCollections"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCreditManagerTableset:
   def __init__(self, obj):
      self.CMCustomer:list[Erp_Tablesets_CMCustomerRow] = obj["CMCustomer"]
      self.CustomCrdPool:list[Erp_Tablesets_CustomCrdPoolRow] = obj["CustomCrdPool"]
      self.GlbCustCred:list[Erp_Tablesets_GlbCustCredRow] = obj["GlbCustCred"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportCustCreditFile_input:
   """ Required : 
   inpFileName
   inpIncludeZero
   pNumberFormat
   """  
   def __init__(self, obj):
      self.inpFileName:str = obj["inpFileName"]
      """  Name that the exported file will have assigned to it  """  
      self.inpIncludeZero:bool = obj["inpIncludeZero"]
      """  A logical flag to indicate whether to include 0 Credit Limit Customers.  """  
      self.pNumberFormat:str = obj["pNumberFormat"]
      """  Number Format American/European.  """  
      pass

class ExportCustCreditFile_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExportCustCredTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ExportCustCredit_input:
   """ Required : 
   inpIncludeZero
   pNumberFormat
   """  
   def __init__(self, obj):
      self.inpIncludeZero:bool = obj["inpIncludeZero"]
      """  A logical flag to indicate whether to include 0 Credit Limit Customers.  """  
      self.pNumberFormat:str = obj["pNumberFormat"]
      """  Number Format American/European.  """  
      pass

class ExportCustCredit_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExportCustCredTableset] = obj["returnObj"]
      pass

class GetARLOC_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class GetARLOC_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARLOCTableset] = obj["returnObj"]
      pass

class GetByCustID_input:
   """ Required : 
   custID
   """  
   def __init__(self, obj):
      self.custID:str = obj["custID"]
      """  The customer character ID  """  
      pass

class GetByCustID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
      pass

class GetCashDeposits_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class GetCashDeposits_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AllocDepositsTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetContacts_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class GetContacts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustCntTableset] = obj["returnObj"]
      pass

class GetCustomerBalance_input:
   """ Required : 
   custNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      pass

class GetCustomerBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.balance:int = obj["parameters"]
      self.rpt1Balance:int = obj["parameters"]
      self.rpt2Balance:int = obj["parameters"]
      self.rpt3Balance:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCustomerGlobalFields_input:
   """ Required : 
   CustNum
   GlobalLock
   """  
   def __init__(self, obj):
      self.CustNum:int = obj["CustNum"]
      self.GlobalLock:bool = obj["GlobalLock"]
      pass

class GetCustomerGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetInvoicedDeposits_input:
   """ Required : 
   ipCustID
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_InvcHeadTableset] = obj["ds1"]
      pass

class GetInvoicedDeposits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_InvcHeadTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class GetInvoicesEx_input:
   """ Required : 
   ipCustID
   mode
   fromDays
   inRange
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      self.mode:str = obj["mode"]
      self.fromDays:int = obj["fromDays"]
      self.inRange:bool = obj["inRange"]
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

class GetInvoicesEx_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcHeadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetInvoices_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

class GetInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvcHeadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_CMCustomerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCMCustomer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class GetNewCMCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlbCustCred_input:
   """ Required : 
   ds
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewGlbCustCred_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOrders_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class GetOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CMOrderHedTableset] = obj["returnObj"]
      pass

class GetPayIns_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      pass

class GetPayIns_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPNHeadTableset] = obj["returnObj"]
      pass

class GetPaymentsDetails_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID of the transaction under which the Invoice was posted  """  
      self.headNum:int = obj["headNum"]
      """  HeadNum, The foreign key that relates this detail record to a CashHead record.  """  
      pass

class GetPaymentsDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashDtlTableset] = obj["returnObj"]
      pass

class GetPaymentsHeaders_input:
   """ Required : 
   ipCustID
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  The customer character ID  """  
      pass

class GetPaymentsHeaders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadTableset] = obj["returnObj"]
      pass

class GetPayments_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

class GetPayments_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CashHeadTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AllocDepositsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCMCustomer
   whereClauseCustomCrdPool
   whereClauseGlbCustCred
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCMCustomer:str = obj["whereClauseCMCustomer"]
      self.whereClauseCustomCrdPool:str = obj["whereClauseCustomCrdPool"]
      self.whereClauseGlbCustCred:str = obj["whereClauseGlbCustCred"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
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

class ImportCustCreditCsv_input:
   """ Required : 
   inFile
   pNumberFormat
   """  
   def __init__(self, obj):
      self.inFile:str = obj["inFile"]
      """  Name of the File imported. i.e. C:\EpicorData\Users\MANAGER\Import\import.csv  """  
      self.pNumberFormat:str = obj["pNumberFormat"]
      """  Number Format American/European.  """  
      pass

class ImportCustCreditCsv_output:
   def __init__(self, obj):
      pass

class ImportCustCredit_input:
   """ Required : 
   ds
   pNumberFormat
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportCustCredTableset] = obj["ds"]
      self.pNumberFormat:str = obj["pNumberFormat"]
      """  Number Format American/European.  """  
      pass

class ImportCustCredit_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditManagerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportCustCredTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PESelectInvoices_input:
   """ Required : 
   custNum
   collectionsDate
   dsPEARInvSel
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer No  """  
      self.collectionsDate:str = obj["collectionsDate"]
      """  Collections Date  """  
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelBOTableset] = obj["dsPEARInvSel"]
      pass

class PESelectInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelBOTableset] = obj["dsPEARInvSel"]
      pass

      """  output parameters  """  

class PEUpdateInvcHeadRecords_input:
   """ Required : 
   custNum
   dsPEARInvSel
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      """  Customer No  """  
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelBOTableset] = obj["dsPEARInvSel"]
      pass

class PEUpdateInvcHeadRecords_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.dsPEARInvSel:list[Erp_Tablesets_PEARInvSelBOTableset] = obj["dsPEARInvSel"]
      pass

      """  output parameters  """  

class SetOrdersCreditOverride_input:
   """ Required : 
   btcustNum
   """  
   def __init__(self, obj):
      self.btcustNum:int = obj["btcustNum"]
      pass

class SetOrdersCreditOverride_output:
   def __init__(self, obj):
      pass

class UpdateCMOrderHed_input:
   """ Required : 
   ipCustNum
   ds
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  The customer Num  """  
      self.ds:list[Erp_Tablesets_CMOrderHedTableset] = obj["ds"]
      pass

class UpdateCMOrderHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CMOrderHedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateCreditTotals_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class UpdateCreditTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCreditManagerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCreditManagerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateGlobalLimits_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class UpdateGlobalLimits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateNACreditPrc_input:
   """ Required : 
   status
   fieldName
   ds
   """  
   def __init__(self, obj):
      self.status:bool = obj["status"]
      """  Bool parameter to know if used/share (true) or unUsed/notShared (false)  """  
      self.fieldName:str = obj["fieldName"]
      """  NACreditPrc field name to be reset  """  
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class UpdateNACreditPrc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditManagerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAgingCode_input:
   """ Required : 
   ipAgingCode
   """  
   def __init__(self, obj):
      self.ipAgingCode:str = obj["ipAgingCode"]
      """  Aging Code  """  
      pass

class ValidateAgingCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateGlbNACreditSharedPrc_input:
   """ Required : 
   creditSharedPrc
   """  
   def __init__(self, obj):
      self.creditSharedPrc:int = obj["creditSharedPrc"]
      """  Value to be validated  """  
      pass

class ValidateGlbNACreditSharedPrc_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateGlbNAParentCreditPrc_input:
   """ Required : 
   parentCreditPrc
   """  
   def __init__(self, obj):
      self.parentCreditPrc:int = obj["parentCreditPrc"]
      """  Value to be validated  """  
      pass

class ValidateGlbNAParentCreditPrc_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateNACreditSharedPrc_input:
   """ Required : 
   creditSharedPrc
   """  
   def __init__(self, obj):
      self.creditSharedPrc:int = obj["creditSharedPrc"]
      """  Value to be validated  """  
      pass

class ValidateNACreditSharedPrc_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateNAParentCreditPrc_input:
   """ Required : 
   parentCreditPrc
   """  
   def __init__(self, obj):
      self.parentCreditPrc:int = obj["parentCreditPrc"]
      """  Value to be validated  """  
      pass

class ValidateNAParentCreditPrc_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class isNAGlobalCustomer_input:
   """ Required : 
   ipCustNum
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      pass

class isNAGlobalCustomer_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

