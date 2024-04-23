import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfiguratorUDFuncsSvc
# Description: This Business Object allows the modification of Configurator User Defined Functions
            This Object is intent to replace the calls to Customer own code in .i and .p files with User Defined Functions in C#
           
            Business Object for the Configurator User Defined Functions Entry
            Alejandro Martinez
            08/26/2013
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorUDFuncs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfiguratorUDFuncs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorUDFuncs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs",headers=creds) as resp:
           return await resp.json()

async def post_ConfiguratorUDFuncs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorUDFuncs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company, ConfigID, FunctionName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfiguratorUDFunc item
   Description: Calls GetByID to retrieve the ConfiguratorUDFunc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorUDFunc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company, ConfigID, FunctionName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfiguratorUDFunc for the service
   Description: Calls UpdateExt to update ConfiguratorUDFunc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorUDFunc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfiguratorUDFuncs_Company_ConfigID_FunctionName(Company, ConfigID, FunctionName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfiguratorUDFunc item
   Description: Call UpdateExt to delete ConfiguratorUDFunc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorUDFunc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName_PcFunctionDefAttches(Company, ConfigID, FunctionName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcFunctionDefAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcFunctionDefAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")/PcFunctionDefAttches",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorUDFuncs_Company_ConfigID_FunctionName_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company, ConfigID, FunctionName, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcFunctionDefAttch item
   Description: Calls GetByID to retrieve the PcFunctionDefAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionDefAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/ConfiguratorUDFuncs(" + Company + "," + ConfigID + "," + FunctionName + ")/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcFunctionDefAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcFunctionDefAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcFunctionDefAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches",headers=creds) as resp:
           return await resp.json()

async def post_PcFunctionDefAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcFunctionDefAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company, ConfigID, FunctionName, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcFunctionDefAttch item
   Description: Calls GetByID to retrieve the PcFunctionDefAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionDefAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company, ConfigID, FunctionName, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcFunctionDefAttch for the service
   Description: Calls UpdateExt to update PcFunctionDefAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcFunctionDefAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionDefAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcFunctionDefAttches_Company_ConfigID_FunctionName_DrawingSeq(Company, ConfigID, FunctionName, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcFunctionDefAttch item
   Description: Call UpdateExt to delete PcFunctionDefAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcFunctionDefAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionDefAttches(" + Company + "," + ConfigID + "," + FunctionName + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcFunctionParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcFunctionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcFunctionParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams",headers=creds) as resp:
           return await resp.json()

async def post_PcFunctionParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcFunctionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company, ConfigID, FunctionName, ParameterName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcFunctionParam item
   Description: Calls GetByID to retrieve the PcFunctionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcFunctionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company, ConfigID, FunctionName, ParameterName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcFunctionParam for the service
   Description: Calls UpdateExt to update PcFunctionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcFunctionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcFunctionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcFunctionParams_Company_ConfigID_FunctionName_ParameterName(Company, ConfigID, FunctionName, ParameterName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcFunctionParam item
   Description: Call UpdateExt to delete PcFunctionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcFunctionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param FunctionName: Desc: FunctionName   Required: True   Allow empty value : True
      :param ParameterName: Desc: ParameterName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/PcFunctionParams(" + Company + "," + ConfigID + "," + FunctionName + "," + ParameterName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcFunctionDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcFunctionDef, whereClausePcFunctionDefAttch, whereClausePcFunctionParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePcFunctionDef=" + whereClausePcFunctionDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcFunctionDefAttch=" + whereClausePcFunctionDefAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcFunctionParam=" + whereClausePcFunctionParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, functionName, epicorHeaders = None):
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
   params += "configID=" + configID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "functionName=" + functionName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidateConfigID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateConfigID
   Description: Validates if the configuration ID Exist in the Catalog.
   OperationID: ValidateConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateConfigForCopyMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateConfigForCopyMethod
   Description: Verify the method being copied is valid for the target configuration
   OperationID: ValidateConfigForCopyMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateConfigForCopyMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateConfigForCopyMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveOnePosition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveOnePosition
   Description: This Method moves Up and Down Parameter for User Defined Functions one possitio
in the grid and returns the whole updated DataTable
   OperationID: MoveOnePosition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveOnePosition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveOnePosition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoGetNewParamSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoGetNewParamSequence
   Description: This Method Returns the corresponding new Parameter Sequence for the new Parameter.
   OperationID: DoGetNewParamSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoGetNewParamSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoGetNewParamSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFunctionTypeChanges(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFunctionTypeChanges
   Description: Executes the IsTheMethodInUse logic and checks EWC types to inform user typescript code will be reset to string.empty when changing from client to server.
   OperationID: ValidateFunctionTypeChanges
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFunctionTypeChanges_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFunctionTypeChanges_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePcFunctionParamBeforeDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePcFunctionParamBeforeDelete
   Description: Determine if the method is in use before deleting the parameter so the appropriate warning can be presented to the user
   OperationID: ValidatePcFunctionParamBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcFunctionParamBeforeDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcFunctionParamBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsTheMethodInUse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsTheMethodInUse
   Description: Use this method to determine if a method is in use prior to renaming it
   OperationID: IsTheMethodInUse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsTheMethodInUse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTheMethodInUse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RenameMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RenameMethod
   Description: This Method Renames the User Defined Method name.
   OperationID: RenameMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RenameMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RenameMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyMethod
   Description: This Method Copies a user defined method to a different Configurator.
   OperationID: CopyMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateName
   Description: This method Validates if the specified string contains spaces in there and throws an exception in that case.
   OperationID: ValidateName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMethod
   Description: This method Validates if the specified method already exist in the target configurator.
   OperationID: ValidateMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEWCReturnType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEWCReturnType
   Description: This method Validates if the return type is valid for the type of configurator and the type of function defined
   OperationID: ValidateEWCReturnType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEWCReturnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEWCReturnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetParametersForCodeEditor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetParametersForCodeEditor
   Description: Returns a list of all the parameters within the Method specified.
   OperationID: GetParametersForCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParametersForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveNewCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveNewCode
   Description: This method Saves the expression code returned from Code Editor.
   OperationID: SaveNewCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveNewCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveNewCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveNewScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveNewScriptCode
   Description: This method Saves the Script expression code returned from Code Editor for client UDMethods.
   OperationID: SaveNewScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveNewScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveNewScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFunctionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFunctionType
   Description: Set SendValues when function type changes
   OperationID: OnChangeFunctionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFunctionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFunctionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MethodUsesInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MethodUsesInputs
   Description: Set SendValues when function type changes
   OperationID: MethodUsesInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MethodUsesInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodUsesInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUDMethodsForCodeEditor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUDMethodsForCodeEditor
   Description: retrieves data needed by the Code Editor
   OperationID: GetUDMethodsForCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUDMethodsForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUDMethodsForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcFunctionDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcFunctionDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcFunctionDefAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcFunctionDefAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionDefAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionDefAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionDefAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcFunctionParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcFunctionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcFunctionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcFunctionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcFunctionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorUDFuncsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcFunctionDefAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcFunctionDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcFunctionDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcFunctionParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcFunctionParamRow] = obj["value"]
      pass

class Erp_Tablesets_PcFunctionDefAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionName:str = obj["FunctionName"]
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

class Erp_Tablesets_PcFunctionDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.FunctionType:str = obj["FunctionType"]
      """  FunctionType  """  
      self.ReturnType:str = obj["ReturnType"]
      """  ReturnType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ParamsExist:bool = obj["ParamsExist"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.FunctionType:str = obj["FunctionType"]
      """  FunctionType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ReturnType:str = obj["ReturnType"]
      """  ReturnType  """  
      self.OldFunctionName:str = obj["OldFunctionName"]
      """  OldFunctionName  """  
      self.IsSync:bool = obj["IsSync"]
      """  IsSync  """  
      self.GlobalFunc:bool = obj["GlobalFunc"]
      """  GlobalFunc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BagID:str = obj["BagID"]
      """  BagID  """  
      self.NoInputs:bool = obj["NoInputs"]
      """  NoInputs  """  
      self.ScriptExpression:str = obj["ScriptExpression"]
      """  ScriptExpression  """  
      self.DispFunctionName:str = obj["DispFunctionName"]
      self.DispFunctionType:str = obj["DispFunctionType"]
      self.DispReturnType:str = obj["DispReturnType"]
      self.BtnEditScript:bool = obj["BtnEditScript"]
      """  Script expressions are only permitted for PCEMF configurator client expressions.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.ParameterName:str = obj["ParameterName"]
      """  ParameterName  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.Modifier:str = obj["Modifier"]
      """  Modifier  """  
      self.ParamType:str = obj["ParamType"]
      """  ParamType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ParamSeq:int = obj["ParamSeq"]
      """  ParamSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CopyMethod_input:
   """ Required : 
   sourceConfigID
   sourceMethodName
   targetConfigID
   targetMethodName
   ds
   """  
   def __init__(self, obj):
      self.sourceConfigID:str = obj["sourceConfigID"]
      """  This the source Configuration ID  """  
      self.sourceMethodName:str = obj["sourceMethodName"]
      """  This is the source method Name  """  
      self.targetConfigID:str = obj["targetConfigID"]
      """  This os the new Method  """  
      self.targetMethodName:str = obj["targetMethodName"]
      """  This is the Original method Name  """  
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

class CopyMethod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   configID
   functionName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.functionName:str = obj["functionName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DoGetNewParamSequence_input:
   """ Required : 
   configID
   functionName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.functionName:str = obj["functionName"]
      """  Function or Method Name  """  
      pass

class DoGetNewParamSequence_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  The new Sequence  """  
      pass

class Erp_Tablesets_CodeEditorPCFuncParamRow:
   def __init__(self, obj):
      self.ParameterName:str = obj["ParameterName"]
      self.ParameterType:str = obj["ParameterType"]
      self.Modifier:str = obj["Modifier"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCInputsRow:
   def __init__(self, obj):
      self.InputName:str = obj["InputName"]
      self.InputType:str = obj["InputType"]
      self.DataType:str = obj["DataType"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigUDCodEditorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionName:str = obj["FunctionName"]
      self.MethodDeclaration:str = obj["MethodDeclaration"]
      self.MethodToolTip:str = obj["MethodToolTip"]
      self.DataType:str = obj["DataType"]
      self.TokenizedText:str = obj["TokenizedText"]
      """  The tokenized text used for the expression builder.  """  
      self.MethodType:str = obj["MethodType"]
      self.CodeEditorText:str = obj["CodeEditorText"]
      self.ExcludeFromExpressionBuilder:bool = obj["ExcludeFromExpressionBuilder"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigUDCodeEditorTableset:
   def __init__(self, obj):
      self.ConfigUDCodEditor:list[Erp_Tablesets_ConfigUDCodEditorRow] = obj["ConfigUDCodEditor"]
      self.CodeEditorPCFuncParam:list[Erp_Tablesets_CodeEditorPCFuncParamRow] = obj["CodeEditorPCFuncParam"]
      self.CodeEditorPCInputs:list[Erp_Tablesets_CodeEditorPCInputsRow] = obj["CodeEditorPCInputs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfiguratorUDFuncsListTableset:
   def __init__(self, obj):
      self.PcFunctionDefList:list[Erp_Tablesets_PcFunctionDefListRow] = obj["PcFunctionDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfiguratorUDFuncsTableset:
   def __init__(self, obj):
      self.PcFunctionDef:list[Erp_Tablesets_PcFunctionDefRow] = obj["PcFunctionDef"]
      self.PcFunctionDefAttch:list[Erp_Tablesets_PcFunctionDefAttchRow] = obj["PcFunctionDefAttch"]
      self.PcFunctionParam:list[Erp_Tablesets_PcFunctionParamRow] = obj["PcFunctionParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcFunctionDefAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionName:str = obj["FunctionName"]
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

class Erp_Tablesets_PcFunctionDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.FunctionType:str = obj["FunctionType"]
      """  FunctionType  """  
      self.ReturnType:str = obj["ReturnType"]
      """  ReturnType  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ParamsExist:bool = obj["ParamsExist"]
      self.ExtConfig:bool = obj["ExtConfig"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.FunctionType:str = obj["FunctionType"]
      """  FunctionType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ReturnType:str = obj["ReturnType"]
      """  ReturnType  """  
      self.OldFunctionName:str = obj["OldFunctionName"]
      """  OldFunctionName  """  
      self.IsSync:bool = obj["IsSync"]
      """  IsSync  """  
      self.GlobalFunc:bool = obj["GlobalFunc"]
      """  GlobalFunc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BagID:str = obj["BagID"]
      """  BagID  """  
      self.NoInputs:bool = obj["NoInputs"]
      """  NoInputs  """  
      self.ScriptExpression:str = obj["ScriptExpression"]
      """  ScriptExpression  """  
      self.DispFunctionName:str = obj["DispFunctionName"]
      self.DispFunctionType:str = obj["DispFunctionType"]
      self.DispReturnType:str = obj["DispReturnType"]
      self.BtnEditScript:bool = obj["BtnEditScript"]
      """  Script expressions are only permitted for PCEMF configurator client expressions.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PcStatusApproved:bool = obj["PcStatusApproved"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcFunctionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FunctionName:str = obj["FunctionName"]
      """  FunctionName  """  
      self.ParameterName:str = obj["ParameterName"]
      """  ParameterName  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.Modifier:str = obj["Modifier"]
      """  Modifier  """  
      self.ParamType:str = obj["ParamType"]
      """  ParamType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ParamSeq:int = obj["ParamSeq"]
      """  ParamSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset:
   def __init__(self, obj):
      self.PcFunctionDef:list[Erp_Tablesets_PcFunctionDefRow] = obj["PcFunctionDef"]
      self.PcFunctionDefAttch:list[Erp_Tablesets_PcFunctionDefAttchRow] = obj["PcFunctionDefAttch"]
      self.PcFunctionParam:list[Erp_Tablesets_PcFunctionParamRow] = obj["PcFunctionParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   configID
   functionName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.functionName:str = obj["functionName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcFunctionDefAttch_input:
   """ Required : 
   ds
   configID
   functionName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.functionName:str = obj["functionName"]
      pass

class GetNewPcFunctionDefAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcFunctionDef_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcFunctionDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcFunctionParam_input:
   """ Required : 
   ds
   configID
   functionName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.functionName:str = obj["functionName"]
      pass

class GetNewPcFunctionParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetParametersForCodeEditor_input:
   """ Required : 
   configID
   functionName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configudation ID  """  
      self.functionName:str = obj["functionName"]
      """  Method Name  """  
      pass

class GetParametersForCodeEditor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigUDCodeEditorTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePcFunctionDef
   whereClausePcFunctionDefAttch
   whereClausePcFunctionParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcFunctionDef:str = obj["whereClausePcFunctionDef"]
      self.whereClausePcFunctionDefAttch:str = obj["whereClausePcFunctionDefAttch"]
      self.whereClausePcFunctionParam:str = obj["whereClausePcFunctionParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUDMethodsForCodeEditor_input:
   """ Required : 
   ConfigID
   FunctionType
   fromUDMethods
   """  
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionType:str = obj["FunctionType"]
      self.fromUDMethods:bool = obj["fromUDMethods"]
      pass

class GetUDMethodsForCodeEditor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigUDCodeEditorTableset] = obj["returnObj"]
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

class IsTheMethodInUse_input:
   """ Required : 
   configID
   currentMethodName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.currentMethodName:str = obj["currentMethodName"]
      pass

class IsTheMethodInUse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inUseMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MethodUsesInputs_input:
   """ Required : 
   configID
   methodName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configurator's id.  """  
      self.methodName:str = obj["methodName"]
      """  The method's name  """  
      pass

class MethodUsesInputs_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class MoveOnePosition_input:
   """ Required : 
   configID
   functionName
   parameterName
   paramSeq
   moveDir
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.functionName:str = obj["functionName"]
      """  Function or Method Name  """  
      self.parameterName:str = obj["parameterName"]
      """  Parameter Name  """  
      self.paramSeq:int = obj["paramSeq"]
      """  Current Sequence of the Parameter being moved  """  
      self.moveDir:str = obj["moveDir"]
      """  Direction to move the Parameter "Up" or "Down"  """  
      pass

class MoveOnePosition_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
      pass

class OnChangeFunctionType_input:
   """ Required : 
   inputName
   ds
   """  
   def __init__(self, obj):
      self.inputName:str = obj["inputName"]
      """  The control name.  """  
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

class OnChangeFunctionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RenameMethod_input:
   """ Required : 
   configID
   oldMethodName
   newMethodName
   ds
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  This os the new Method  """  
      self.oldMethodName:str = obj["oldMethodName"]
      """  This is the Original method Name  """  
      self.newMethodName:str = obj["newMethodName"]
      """  This os the new Method  """  
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

class RenameMethod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["returnObj"]
      pass

class SaveNewCode_input:
   """ Required : 
   configID
   functionName
   newCode
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.functionName:str = obj["functionName"]
      """  Function Name  """  
      self.newCode:str = obj["newCode"]
      """  New Expression Code to be saved  """  
      pass

class SaveNewCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true/False depending if the  """  
      pass

class SaveNewScriptCode_input:
   """ Required : 
   configID
   functionName
   newCode
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.functionName:str = obj["functionName"]
      """  Function Name  """  
      self.newCode:str = obj["newCode"]
      """  New Expression Code to be saved  """  
      pass

class SaveNewScriptCode_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true/False depending if the  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorUDFuncsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorUDFuncsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateConfigForCopyMethod_input:
   """ Required : 
   sourceConfigID
   sourceMethod
   targetConfigID
   """  
   def __init__(self, obj):
      self.sourceConfigID:str = obj["sourceConfigID"]
      self.sourceMethod:str = obj["sourceMethod"]
      self.targetConfigID:str = obj["targetConfigID"]
      pass

class ValidateConfigForCopyMethod_output:
   def __init__(self, obj):
      pass

class ValidateConfigID_input:
   """ Required : 
   proposedConfigID
   """  
   def __init__(self, obj):
      self.proposedConfigID:str = obj["proposedConfigID"]
      pass

class ValidateConfigID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.configApproved:bool = obj["configApproved"]
      self.configType:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateEWCReturnType_input:
   """ Required : 
   functionType
   returnType
   """  
   def __init__(self, obj):
      self.functionType:str = obj["functionType"]
      """  This is the function type: client or server  """  
      self.returnType:str = obj["returnType"]
      """  This is the return type used for the function  """  
      pass

class ValidateEWCReturnType_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateFunctionTypeChanges_input:
   """ Required : 
   configID
   currentMethodName
   proposedFunctionType
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.currentMethodName:str = obj["currentMethodName"]
      """  method being validated  """  
      self.proposedFunctionType:str = obj["proposedFunctionType"]
      """  proposed function type - server or client  """  
      pass

class ValidateFunctionTypeChanges_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inUseMessage:str = obj["parameters"]
      self.EWCWarningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateMethod_input:
   """ Required : 
   configID
   methodName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  This is target or destination Configurator where the method will be copied.  """  
      self.methodName:str = obj["methodName"]
      """  The name of the target method.  """  
      pass

class ValidateMethod_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateName_input:
   """ Required : 
   name
   from
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      """  String provided for a MethodName or ParameterName.  """  
      self.from:str = obj["from"]
      """  Indicates if the name belongs to a method or parameter.  """  
      pass

class ValidateName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidatePcFunctionParamBeforeDelete_input:
   """ Required : 
   configID
   functionName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.functionName:str = obj["functionName"]
      pass

class ValidatePcFunctionParamBeforeDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inUseMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

