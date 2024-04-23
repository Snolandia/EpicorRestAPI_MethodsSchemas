import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ElectronicInterfaceSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicInterfaces(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ElectronicInterfaces items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ElectronicInterfaces
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces",headers=creds) as resp:
           return await resp.json()

async def post_ElectronicInterfaces(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ElectronicInterfaces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EFTHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EFTHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ElectronicInterfaces_Company_EFTHeadUID(Company, EFTHeadUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ElectronicInterface item
   Description: Calls GetByID to retrieve the ElectronicInterface item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ElectronicInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EFTHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces(" + Company + "," + EFTHeadUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ElectronicInterfaces_Company_EFTHeadUID(Company, EFTHeadUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ElectronicInterface for the service
   Description: Calls UpdateExt to update ElectronicInterface. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ElectronicInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EFTHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces(" + Company + "," + EFTHeadUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ElectronicInterfaces_Company_EFTHeadUID(Company, EFTHeadUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ElectronicInterface item
   Description: Call UpdateExt to delete ElectronicInterface item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ElectronicInterface
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces(" + Company + "," + EFTHeadUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicInterfaces_Company_EFTHeadUID_EFTProps(Company, EFTHeadUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EFTProps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EFTProps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces(" + Company + "," + EFTHeadUID + ")/EFTProps",headers=creds) as resp:
           return await resp.json()

async def get_ElectronicInterfaces_Company_EFTHeadUID_EFTProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EFTProp item
   Description: Calls GetByID to retrieve the EFTProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EFTProp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EFTPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/ElectronicInterfaces(" + Company + "," + EFTHeadUID + ")/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EFTProps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EFTProps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EFTProps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps",headers=creds) as resp:
           return await resp.json()

async def post_EFTProps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EFTProps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EFTPropRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EFTPropRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EFTProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EFTProp item
   Description: Calls GetByID to retrieve the EFTProp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EFTProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EFTPropRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EFTProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EFTProp for the service
   Description: Calls UpdateExt to update EFTProp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EFTProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EFTPropRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EFTProps_Company_EFTHeadUID_EFTPropUID(Company, EFTHeadUID, EFTPropUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EFTProp item
   Description: Call UpdateExt to delete EFTProp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EFTProp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EFTProps_Company_EFTHeadUID_EFTPropUID_EFTPropVals(Company, EFTHeadUID, EFTPropUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EFTPropVals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EFTPropVals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTPropValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")/EFTPropVals",headers=creds) as resp:
           return await resp.json()

async def get_EFTProps_Company_EFTHeadUID_EFTPropUID_EFTPropVals_Company_EFTHeadUID_EFTPropUID_EFTPropValUID(Company, EFTHeadUID, EFTPropUID, EFTPropValUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EFTPropVal item
   Description: Calls GetByID to retrieve the EFTPropVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EFTPropVal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param EFTPropValUID: Desc: EFTPropValUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EFTPropValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTProps(" + Company + "," + EFTHeadUID + "," + EFTPropUID + ")/EFTPropVals(" + Company + "," + EFTHeadUID + "," + EFTPropUID + "," + EFTPropValUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EFTPropVals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EFTPropVals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EFTPropVals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTPropValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTPropVals",headers=creds) as resp:
           return await resp.json()

async def post_EFTPropVals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EFTPropVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EFTPropValRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EFTPropValRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTPropVals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EFTPropVals_Company_EFTHeadUID_EFTPropUID_EFTPropValUID(Company, EFTHeadUID, EFTPropUID, EFTPropValUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EFTPropVal item
   Description: Calls GetByID to retrieve the EFTPropVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EFTPropVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param EFTPropValUID: Desc: EFTPropValUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EFTPropValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTPropVals(" + Company + "," + EFTHeadUID + "," + EFTPropUID + "," + EFTPropValUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EFTPropVals_Company_EFTHeadUID_EFTPropUID_EFTPropValUID(Company, EFTHeadUID, EFTPropUID, EFTPropValUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EFTPropVal for the service
   Description: Calls UpdateExt to update EFTPropVal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EFTPropVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param EFTPropValUID: Desc: EFTPropValUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EFTPropValRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTPropVals(" + Company + "," + EFTHeadUID + "," + EFTPropUID + "," + EFTPropValUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EFTPropVals_Company_EFTHeadUID_EFTPropUID_EFTPropValUID(Company, EFTHeadUID, EFTPropUID, EFTPropValUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EFTPropVal item
   Description: Call UpdateExt to delete EFTPropVal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EFTPropVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EFTHeadUID: Desc: EFTHeadUID   Required: True
      :param EFTPropUID: Desc: EFTPropUID   Required: True
      :param EFTPropValUID: Desc: EFTPropValUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/EFTPropVals(" + Company + "," + EFTHeadUID + "," + EFTPropUID + "," + EFTPropValUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EFTHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEFTHead, whereClauseEFTProp, whereClauseEFTPropVal, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseEFTHead=" + whereClauseEFTHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEFTProp=" + whereClauseEFTProp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEFTPropVal=" + whereClauseEFTPropVal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(efTHeadUID, epicorHeaders = None):
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
   params += "efTHeadUID=" + efTHeadUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOfProgramCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOfProgramCategory
   Description: This method should be called when the Electronic Interface Program Category is changed.
   OperationID: ChangeOfProgramCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOfProgramCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOfProgramCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOfType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOfType
   Description: This method should be called if the Electronic Interface Type changes.
   OperationID: ChangeOfType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOfType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOfType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByName
   Description: Returns dataset by the interface name.
   OperationID: GetByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIDByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetIDByName
   Description: Returns EFTHeadUID by the interface name.
   OperationID: GetIDByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetIDByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIDByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInterfaceTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetInterfaceTypes
   Description: Returns list of interfaces types defined in TypeNames array
Symbol | will be replaced by ~ on the client side. For using in combos
   OperationID: GetInterfaceTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInterfaceTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetInterfaceTypesDelimitedList(epicorHeaders = None):
   """  
   Summary: Invoke method GetInterfaceTypesDelimitedList
   Description: Returns delimited list of interfaces types defined in TypeNames array
   OperationID: GetInterfaceTypesDelimitedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInterfaceTypesDelimitedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetTypeByName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTypeByName
   Description: Returns interface's type by searching for the TypeName
   OperationID: GetTypeByName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTypeByName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTypeByName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFileNames(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFileNames
   Description: Returns a list of files that can be selected for Program
<param name="ProgramCategory">Program Category:  Indicates search for (D)efault programs or (C)ustomer specific programs</param>
   OperationID: GetFileNames
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileNames_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileNames_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InterfaceCanBeDeleted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InterfaceCanBeDeleted
   OperationID: InterfaceCanBeDeleted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InterfaceCanBeDeleted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InterfaceCanBeDeleted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Returns code description list for the table and field.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateProgramCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateProgramCategory
   Description: This method should be called to validate the Electronic Interface Program Category when it is changing.
   OperationID: ValidateProgramCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateProgramCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateProgramCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Export(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Export
   Description: Export requested EI declaration as untyped DataSet
   OperationID: Export
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Export_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Export_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Import(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Import
   Description: Import EI declaration form untyped DataSet with possible transformation from legacy formats
   OperationID: Import
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Import_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Import_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEFTHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEFTHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEFTHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEFTHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEFTHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEFTProp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEFTProp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEFTProp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEFTProp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEFTProp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEFTPropVal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEFTPropVal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEFTPropVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEFTPropVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEFTPropVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ElectronicInterfaceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EFTHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EFTHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EFTHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EFTHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EFTPropRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EFTPropRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EFTPropValRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EFTPropValRow] = obj["value"]
      pass

class Erp_Tablesets_EFTHeadListRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.Name:str = obj["Name"]
      """  Short name of the interface, it should be unique  """  
      self.Type:int = obj["Type"]
      """   The type of interface with the following options:
?	0 = Bank Interface AP
?	1 = Tax Reporting
?	2 = IntraStat Reporting
?	3 = EU Sales List Reporting
?	4 = Bank Interface AR
?	5 = Bank Interface Payroll  """  
      self.Program:str = obj["Program"]
      """  Indicates the plug-in program name that shall be used for this interface.  """  
      self.Description:str = obj["Description"]
      """  Internal description of the interface, only shown in interface maintenance form.  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  Indicates that it?s an interface delivered with the system. System interfaces shall be read-only  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTHead:bool = obj["GlobalEFTHead"]
      """  Marks this EFTHead as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TypeName:str = obj["TypeName"]
      """  Name of interface type  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTHeadRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.Name:str = obj["Name"]
      """  Short name of the interface, it should be unique  """  
      self.Type:int = obj["Type"]
      """   The type of interface with the following options:
?	0 = Bank Interface AP
?	1 = Tax Reporting
?	2 = IntraStat Reporting
?	3 = EU Sales List Reporting
?	4 = Bank Interface AR
?	5 = Bank Interface Payroll  """  
      self.Program:str = obj["Program"]
      """  Indicates the plug-in program name that shall be used for this interface.  """  
      self.Description:str = obj["Description"]
      """  Internal description of the interface, only shown in interface maintenance form.  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  Indicates that it?s an interface delivered with the system. System interfaces shall be read-only  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTHead:bool = obj["GlobalEFTHead"]
      """  Marks this EFTHead as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgramCategory:str = obj["ProgramCategory"]
      """  ProgramCategory  """  
      self.TypeName:str = obj["TypeName"]
      """  Name of interface type  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTPropRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property  """  
      self.Name:str = obj["Name"]
      """  Short name of the property, it should be unique for the particular template  """  
      self.Type:str = obj["Type"]
      """   This is the type of the property and we need to support some of the most common types as:
String
Decimal
List (List of values defined in separate table)
Logical (will show a check box for true or false)
Date  """  
      self.MaxLength:int = obj["MaxLength"]
      """  The total length of the field  """  
      self.MinLength:int = obj["MinLength"]
      """  The minimum length  """  
      self.NumDec:int = obj["NumDec"]
      """  The number of decimals  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTProp:bool = obj["GlobalEFTProp"]
      """  Marks this EFTProp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTPropValRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property.  """  
      self.EFTPropValUID:int = obj["EFTPropValUID"]
      """  Unique identifier of the EFT property value  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeOfProgramCategory_input:
   """ Required : 
   ProposedProgramCategory
   ds
   """  
   def __init__(self, obj):
      self.ProposedProgramCategory:str = obj["ProposedProgramCategory"]
      """  Proposed Program Category  """  
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

class ChangeOfProgramCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOfType_input:
   """ Required : 
   ProposedType
   ds
   """  
   def __init__(self, obj):
      self.ProposedType:str = obj["ProposedType"]
      """  Proposed Type  """  
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

class ChangeOfType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   efTHeadUID
   """  
   def __init__(self, obj):
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EFTHeadListRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.Name:str = obj["Name"]
      """  Short name of the interface, it should be unique  """  
      self.Type:int = obj["Type"]
      """   The type of interface with the following options:
?	0 = Bank Interface AP
?	1 = Tax Reporting
?	2 = IntraStat Reporting
?	3 = EU Sales List Reporting
?	4 = Bank Interface AR
?	5 = Bank Interface Payroll  """  
      self.Program:str = obj["Program"]
      """  Indicates the plug-in program name that shall be used for this interface.  """  
      self.Description:str = obj["Description"]
      """  Internal description of the interface, only shown in interface maintenance form.  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  Indicates that it?s an interface delivered with the system. System interfaces shall be read-only  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTHead:bool = obj["GlobalEFTHead"]
      """  Marks this EFTHead as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TypeName:str = obj["TypeName"]
      """  Name of interface type  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTHeadListTableset:
   def __init__(self, obj):
      self.EFTHeadList:list[Erp_Tablesets_EFTHeadListRow] = obj["EFTHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EFTHeadRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.Name:str = obj["Name"]
      """  Short name of the interface, it should be unique  """  
      self.Type:int = obj["Type"]
      """   The type of interface with the following options:
?	0 = Bank Interface AP
?	1 = Tax Reporting
?	2 = IntraStat Reporting
?	3 = EU Sales List Reporting
?	4 = Bank Interface AR
?	5 = Bank Interface Payroll  """  
      self.Program:str = obj["Program"]
      """  Indicates the plug-in program name that shall be used for this interface.  """  
      self.Description:str = obj["Description"]
      """  Internal description of the interface, only shown in interface maintenance form.  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  Indicates that it?s an interface delivered with the system. System interfaces shall be read-only  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTHead:bool = obj["GlobalEFTHead"]
      """  Marks this EFTHead as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProgramCategory:str = obj["ProgramCategory"]
      """  ProgramCategory  """  
      self.TypeName:str = obj["TypeName"]
      """  Name of interface type  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTPropRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property  """  
      self.Name:str = obj["Name"]
      """  Short name of the property, it should be unique for the particular template  """  
      self.Type:str = obj["Type"]
      """   This is the type of the property and we need to support some of the most common types as:
String
Decimal
List (List of values defined in separate table)
Logical (will show a check box for true or false)
Date  """  
      self.MaxLength:int = obj["MaxLength"]
      """  The total length of the field  """  
      self.MinLength:int = obj["MinLength"]
      """  The minimum length  """  
      self.NumDec:int = obj["NumDec"]
      """  The number of decimals  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlobalEFTProp:bool = obj["GlobalEFTProp"]
      """  Marks this EFTProp as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EFTPropValRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT  """  
      self.EFTPropUID:int = obj["EFTPropUID"]
      """  Unique identifier of the EFT property.  """  
      self.EFTPropValUID:int = obj["EFTPropValUID"]
      """  Unique identifier of the EFT property value  """  
      self.PropValue:str = obj["PropValue"]
      """  Property Value, always defined as string value  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicInterfaceFilesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DirectoryName:str = obj["DirectoryName"]
      self.FileName:str = obj["FileName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ElectronicInterfaceFilesTableset:
   def __init__(self, obj):
      self.ElectronicInterfaceFiles:list[Erp_Tablesets_ElectronicInterfaceFilesRow] = obj["ElectronicInterfaceFiles"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ElectronicInterfaceTableset:
   def __init__(self, obj):
      self.EFTHead:list[Erp_Tablesets_EFTHeadRow] = obj["EFTHead"]
      self.EFTProp:list[Erp_Tablesets_EFTPropRow] = obj["EFTProp"]
      self.EFTPropVal:list[Erp_Tablesets_EFTPropValRow] = obj["EFTPropVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtElectronicInterfaceTableset:
   def __init__(self, obj):
      self.EFTHead:list[Erp_Tablesets_EFTHeadRow] = obj["EFTHead"]
      self.EFTProp:list[Erp_Tablesets_EFTPropRow] = obj["EFTProp"]
      self.EFTPropVal:list[Erp_Tablesets_EFTPropValRow] = obj["EFTPropVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Export_input:
   """ Required : 
   companyID
   eftHeadUID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.eftHeadUID:int = obj["eftHeadUID"]
      pass

class Export_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetByID_input:
   """ Required : 
   efTHeadUID
   """  
   def __init__(self, obj):
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["returnObj"]
      pass

class GetByName_input:
   """ Required : 
   name
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      """  interface name  """  
      pass

class GetByName_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name.  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFileNames_input:
   """ Required : 
   ProgramCategory
   """  
   def __init__(self, obj):
      self.ProgramCategory:str = obj["ProgramCategory"]
      pass

class GetFileNames_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceFilesTableset] = obj["returnObj"]
      pass

class GetIDByName_input:
   """ Required : 
   name
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      """  interface name  """  
      pass

class GetIDByName_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  The full DataSet.  """  
      pass

class GetInterfaceTypesDelimitedList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Delimited list of interface types defined in TypeNames array  """  
      pass

class GetInterfaceTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.list:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_EFTHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEFTHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

class GetNewEFTHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEFTPropVal_input:
   """ Required : 
   ds
   efTHeadUID
   efTPropUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      self.efTHeadUID:int = obj["efTHeadUID"]
      self.efTPropUID:int = obj["efTPropUID"]
      pass

class GetNewEFTPropVal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEFTProp_input:
   """ Required : 
   ds
   efTHeadUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      self.efTHeadUID:int = obj["efTHeadUID"]
      pass

class GetNewEFTProp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEFTHead
   whereClauseEFTProp
   whereClauseEFTPropVal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEFTHead:str = obj["whereClauseEFTHead"]
      self.whereClauseEFTProp:str = obj["whereClauseEFTProp"]
      self.whereClauseEFTPropVal:str = obj["whereClauseEFTPropVal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTypeByName_input:
   """ Required : 
   typeName
   """  
   def __init__(self, obj):
      self.typeName:str = obj["typeName"]
      """  TypeName for interfaces type  """  
      pass

class GetTypeByName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.typeID:int = obj["parameters"]
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

class Import_input:
   """ Required : 
   version
   data
   """  
   def __init__(self, obj):
      self.version:str = obj["version"]
      self.data      #schema had no properties on an object.
      pass

class Import_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  DataSet describing changes in Primary Keys of imported items  """  
      pass

class InterfaceCanBeDeleted_input:
   """ Required : 
   headUID
   """  
   def __init__(self, obj):
      self.headUID:int = obj["headUID"]
      """  electronic interface identifier  """  
      pass

class InterfaceCanBeDeleted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.canbe:bool = obj["canbe"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtElectronicInterfaceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtElectronicInterfaceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateProgramCategory_input:
   """ Required : 
   ProposedProgramCategory
   ds
   """  
   def __init__(self, obj):
      self.ProposedProgramCategory:str = obj["ProposedProgramCategory"]
      """  Proposed Program Category  """  
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

class ValidateProgramCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ElectronicInterfaceTableset] = obj["ds"]
      pass

      """  output parameters  """  

