import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QMarkUpSvc
# Description: Quote Mark up master. This file contains records that provide default
markup percentages for quoting. One of these defaults can be established
as the system default (see EQSyst). Also they can be associated to specific
customers.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QMarkUps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QMarkUps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QMarkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps",headers=creds) as resp:
           return await resp.json()

async def post_QMarkUps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QMarkUps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QMarkUpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QMarkUpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps_Company_MarkUpID(Company, MarkUpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QMarkUp item
   Description: Calls GetByID to retrieve the QMarkUp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QMarkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QMarkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QMarkUps_Company_MarkUpID(Company, MarkUpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QMarkUp for the service
   Description: Calls UpdateExt to update QMarkUp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QMarkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QMarkUpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QMarkUps_Company_MarkUpID(Company, MarkUpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QMarkUp item
   Description: Call UpdateExt to delete QMarkUp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QMarkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps_Company_MarkUpID_Qmmkups(Company, MarkUpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Qmmkups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Qmmkups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")/Qmmkups",headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps_Company_MarkUpID_Qmmkups_Company_MarkUpID_ClassCode(Company, MarkUpID, ClassCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Qmmkup item
   Description: Calls GetByID to retrieve the Qmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qmmkup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")/Qmmkups(" + Company + "," + MarkUpID + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps_Company_MarkUpID_PrjMkUps(Company, MarkUpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PrjMkUps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PrjMkUps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjMkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")/PrjMkUps",headers=creds) as resp:
           return await resp.json()

async def get_QMarkUps_Company_MarkUpID_PrjMkUps_Company_MarkUpID_RoleCd(Company, MarkUpID, RoleCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PrjMkUp item
   Description: Calls GetByID to retrieve the PrjMkUp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjMkUp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PrjMkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/QMarkUps(" + Company + "," + MarkUpID + ")/PrjMkUps(" + Company + "," + MarkUpID + "," + RoleCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_Qmmkups(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Qmmkups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Qmmkups
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/Qmmkups",headers=creds) as resp:
           return await resp.json()

async def post_Qmmkups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Qmmkups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QmmkupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QmmkupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/Qmmkups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Qmmkups_Company_MarkUpID_ClassCode(Company, MarkUpID, ClassCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Qmmkup item
   Description: Calls GetByID to retrieve the Qmmkup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Qmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QmmkupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/Qmmkups(" + Company + "," + MarkUpID + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Qmmkups_Company_MarkUpID_ClassCode(Company, MarkUpID, ClassCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Qmmkup for the service
   Description: Calls UpdateExt to update Qmmkup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Qmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QmmkupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/Qmmkups(" + Company + "," + MarkUpID + "," + ClassCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Qmmkups_Company_MarkUpID_ClassCode(Company, MarkUpID, ClassCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Qmmkup item
   Description: Call UpdateExt to delete Qmmkup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Qmmkup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param ClassCode: Desc: ClassCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/Qmmkups(" + Company + "," + MarkUpID + "," + ClassCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PrjMkUps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PrjMkUps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PrjMkUps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjMkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/PrjMkUps",headers=creds) as resp:
           return await resp.json()

async def post_PrjMkUps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PrjMkUps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PrjMkUpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PrjMkUpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/PrjMkUps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PrjMkUps_Company_MarkUpID_RoleCd(Company, MarkUpID, RoleCd, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PrjMkUp item
   Description: Calls GetByID to retrieve the PrjMkUp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjMkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PrjMkUpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/PrjMkUps(" + Company + "," + MarkUpID + "," + RoleCd + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PrjMkUps_Company_MarkUpID_RoleCd(Company, MarkUpID, RoleCd, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PrjMkUp for the service
   Description: Calls UpdateExt to update PrjMkUp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PrjMkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PrjMkUpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/PrjMkUps(" + Company + "," + MarkUpID + "," + RoleCd + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PrjMkUps_Company_MarkUpID_RoleCd(Company, MarkUpID, RoleCd, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PrjMkUp item
   Description: Call UpdateExt to delete PrjMkUp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PrjMkUp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MarkUpID: Desc: MarkUpID   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/PrjMkUps(" + Company + "," + MarkUpID + "," + RoleCd + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QMarkUpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQMarkUp, whereClauseQmmkup, whereClausePrjMkUp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseQMarkUp=" + whereClauseQMarkUp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQmmkup=" + whereClauseQmmkup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePrjMkUp=" + whereClausePrjMkUp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(markUpID, epicorHeaders = None):
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
   params += "markUpID=" + markUpID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpBurdenMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpBurdenMarkUp
   Description: Validate BurdenMarkUp when it is changing.
   OperationID: OnChangeQMarkUpBurdenMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpBurdenMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpBurdenMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpCommissionPct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpCommissionPct
   Description: Validate CommissionPct when it is changing.
   OperationID: OnChangeQMarkUpCommissionPct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpCommissionPct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpCommissionPct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpLaborMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpLaborMarkUp
   Description: Validate LaborMarkUp when it is changing.
   OperationID: OnChangeQMarkUpLaborMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpLaborMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpLaborMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpMaterialMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpMaterialMarkUp
   Description: Validate MaterialMarkUp when it is changing.
   OperationID: OnChangeQMarkUpMaterialMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpMaterialMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpMaterialMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpMiscCostMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpMiscCostMarkUp
   Description: Validate MiscCostMarkUp when it is changing.
   OperationID: OnChangeQMarkUpMiscCostMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpMiscCostMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpMiscCostMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpMtlBurMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpMtlBurMarkUp
   Description: Validate MtlBurMarkUp when it is changing.
   OperationID: OnChangeQMarkUpMtlBurMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpMtlBurMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpMtlBurMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQMarkUpSubcontractMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQMarkUpSubcontractMarkUp
   Description: Validate SubcontractMarkUp when it is changing.
   OperationID: OnChangeQMarkUpSubcontractMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQMarkUpSubcontractMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQMarkUpSubcontractMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQmmkupMaterialMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQmmkupMaterialMarkUp
   Description: Validate MaterialMarkUp when it is changing.
   OperationID: OnChangeQmmkupMaterialMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQmmkupMaterialMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQmmkupMaterialMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQMarkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQMarkUp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQMarkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQMarkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQMarkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQmmkup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQmmkup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQmmkup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQmmkup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQmmkup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPrjMkUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPrjMkUp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPrjMkUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPrjMkUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPrjMkUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QMarkUpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjMkUpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PrjMkUpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QMarkUpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QMarkUpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QMarkUpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QMarkUpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QmmkupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QmmkupRow] = obj["value"]
      pass

class Erp_Tablesets_PrjMkUpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.PrjRoleMarkUp:int = obj["PrjRoleMarkUp"]
      """  Role Mark Up percent  """  
      self.GlobalPrjMkUp:bool = obj["GlobalPrjMkUp"]
      """  Marks this PrjMkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QMarkUpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which material costs will be marked up.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  Percentage at which subcontract costs will be marked up.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Percentage at which labor costs will be marked up.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Percentage at which burden costs will be marked up.  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Percentage at which material burden costs will be marked up.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Percentage at which miscellaneous costs will be marked up.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values.  """  
      self.GlobalQMarkUp:bool = obj["GlobalQMarkUp"]
      """  Marks this QMarkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      """  Is this record a system default ?  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QMarkUpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which material costs will be marked up.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  Percentage at which subcontract costs will be marked up.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Percentage at which labor costs will be marked up.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Percentage at which burden costs will be marked up.  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Percentage at which material burden costs will be marked up.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Percentage at which miscellaneous costs will be marked up.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values.  """  
      self.GlobalQMarkUp:bool = obj["GlobalQMarkUp"]
      """  Marks this QMarkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      """  Is this record a system default ?  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QmmkupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  PartClass.ClassID value of the part class associated with this material markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which materials related to a specific part class (Qmmkup.ClassCode) will be marked up  """  
      self.GlobalQmmkup:bool = obj["GlobalQmmkup"]
      """  Marks this Qmmkup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassCodeDescription:str = obj["ClassCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   markUpID
   """  
   def __init__(self, obj):
      self.markUpID:str = obj["markUpID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PrjMkUpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.PrjRoleMarkUp:int = obj["PrjRoleMarkUp"]
      """  Role Mark Up percent  """  
      self.GlobalPrjMkUp:bool = obj["GlobalPrjMkUp"]
      """  Marks this PrjMkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QMarkUpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which material costs will be marked up.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  Percentage at which subcontract costs will be marked up.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Percentage at which labor costs will be marked up.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Percentage at which burden costs will be marked up.  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Percentage at which material burden costs will be marked up.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Percentage at which miscellaneous costs will be marked up.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values.  """  
      self.GlobalQMarkUp:bool = obj["GlobalQMarkUp"]
      """  Marks this QMarkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      """  Is this record a system default ?  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QMarkUpListTableset:
   def __init__(self, obj):
      self.QMarkUpList:list[Erp_Tablesets_QMarkUpListRow] = obj["QMarkUpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QMarkUpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this markup record assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description of the markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which material costs will be marked up.  """  
      self.SubcontractMarkUp:int = obj["SubcontractMarkUp"]
      """  Percentage at which subcontract costs will be marked up.  """  
      self.LaborMarkUp:int = obj["LaborMarkUp"]
      """  Percentage at which labor costs will be marked up.  """  
      self.BurdenMarkUp:int = obj["BurdenMarkUp"]
      """  Percentage at which burden costs will be marked up.  """  
      self.MtlBurMarkUp:int = obj["MtlBurMarkUp"]
      """  Percentage at which material burden costs will be marked up.  """  
      self.MiscCostMarkUp:int = obj["MiscCostMarkUp"]
      """  Percentage at which miscellaneous costs will be marked up.  """  
      self.CommissionPct:int = obj["CommissionPct"]
      """  Allows entry of commission percent so that it will be considered in the final calculated unit price. The commission percent is calculated as a percent of the "net unit price". Net unit price is the material, subcontract, labor, burden and miscellaneous costs plus their corresponding markups.  """  
      self.PercentType:str = obj["PercentType"]
      """  A qualifier of the Material, SubContract, Labor, Burden and Miscellaneous markup percent values.  """  
      self.GlobalQMarkUp:bool = obj["GlobalQMarkUp"]
      """  Marks this QMarkUp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      """  Is this record a system default ?  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QMarkUpTableset:
   def __init__(self, obj):
      self.QMarkUp:list[Erp_Tablesets_QMarkUpRow] = obj["QMarkUp"]
      self.Qmmkup:list[Erp_Tablesets_QmmkupRow] = obj["Qmmkup"]
      self.PrjMkUp:list[Erp_Tablesets_PrjMkUpRow] = obj["PrjMkUp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QmmkupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Unique identifier of this material markup. Defaults from its parent table Qmarkup.  """  
      self.ClassCode:str = obj["ClassCode"]
      """  PartClass.ClassID value of the part class associated with this material markup.  """  
      self.MaterialMarkUp:int = obj["MaterialMarkUp"]
      """  Percentage at which materials related to a specific part class (Qmmkup.ClassCode) will be marked up  """  
      self.GlobalQmmkup:bool = obj["GlobalQmmkup"]
      """  Marks this Qmmkup as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClassCodeDescription:str = obj["ClassCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtQMarkUpTableset:
   def __init__(self, obj):
      self.QMarkUp:list[Erp_Tablesets_QMarkUpRow] = obj["QMarkUp"]
      self.Qmmkup:list[Erp_Tablesets_QmmkupRow] = obj["Qmmkup"]
      self.PrjMkUp:list[Erp_Tablesets_PrjMkUpRow] = obj["PrjMkUp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   markUpID
   """  
   def __init__(self, obj):
      self.markUpID:str = obj["markUpID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QMarkUpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QMarkUpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QMarkUpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QMarkUpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPrjMkUp_input:
   """ Required : 
   ds
   markUpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      self.markUpID:str = obj["markUpID"]
      pass

class GetNewPrjMkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQMarkUp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class GetNewQMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQmmkup_input:
   """ Required : 
   ds
   markUpID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      self.markUpID:str = obj["markUpID"]
      pass

class GetNewQmmkup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQMarkUp
   whereClauseQmmkup
   whereClausePrjMkUp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQMarkUp:str = obj["whereClauseQMarkUp"]
      self.whereClauseQmmkup:str = obj["whereClauseQmmkup"]
      self.whereClausePrjMkUp:str = obj["whereClausePrjMkUp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QMarkUpTableset] = obj["returnObj"]
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

class OnChangeQMarkUpBurdenMarkUp_input:
   """ Required : 
   ipBurdenMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipBurdenMarkUp:int = obj["ipBurdenMarkUp"]
      """  The proposed BurdenMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpBurdenMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpCommissionPct_input:
   """ Required : 
   ipCommissionPct
   ds
   """  
   def __init__(self, obj):
      self.ipCommissionPct:int = obj["ipCommissionPct"]
      """  The proposed CommissionPct value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpCommissionPct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpLaborMarkUp_input:
   """ Required : 
   ipLaborMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipLaborMarkUp:int = obj["ipLaborMarkUp"]
      """  The proposed LaborMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpLaborMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpMaterialMarkUp_input:
   """ Required : 
   ipMaterialMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipMaterialMarkUp:int = obj["ipMaterialMarkUp"]
      """  The proposed MaterialMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpMaterialMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpMiscCostMarkUp_input:
   """ Required : 
   ipMiscCostMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipMiscCostMarkUp:int = obj["ipMiscCostMarkUp"]
      """  The proposed MiscCostMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpMiscCostMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpMtlBurMarkUp_input:
   """ Required : 
   ipMtlBurMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipMtlBurMarkUp:int = obj["ipMtlBurMarkUp"]
      """  The proposed MtlBurMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpMtlBurMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQMarkUpSubcontractMarkUp_input:
   """ Required : 
   ipSubcontractMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipSubcontractMarkUp:int = obj["ipSubcontractMarkUp"]
      """  The proposed SubcontractMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQMarkUpSubcontractMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQmmkupMaterialMarkUp_input:
   """ Required : 
   ipMaterialMarkUp
   ds
   """  
   def __init__(self, obj):
      self.ipMaterialMarkUp:int = obj["ipMaterialMarkUp"]
      """  The proposed MaterialMarkUp value  """  
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class OnChangeQmmkupMaterialMarkUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQMarkUpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQMarkUpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QMarkUpTableset] = obj["ds"]
      pass

      """  output parameters  """  

